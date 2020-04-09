import argparse
import csv
from dotenv import load_dotenv
import glob
import ipaddress
import ipinfo
import json
import os
import pandas as pd


# CLI Parser
parser = argparse.ArgumentParser(description='The full Monty on filtering MO365 Logs')
parser.add_argument('indir', type=str, help='Input dir for logs')
parser.add_argument('outdir', type=str, help='Output dir for comprehension')
args = parser.parse_args()

indir = args.indir
outdir = args.outdir


# Setup Inbound Log Feed
os.chdir(indir)
extension = "csv"
files = glob.glob('*.{}'.format(extension))


# Setup Outbound Comprehension Location
path = '../'
if not os.path.isdir(outdir):
	os.mkdir(outdir)
outfile = outdir + "/results-GEO.xlsx"


# Setup Cache and Results
cache = {}
results = []


# Setup GeoIP service
#
# https://ipinfo.io/signup - SignUp for Free for 50,000 queries per month
# Place API token in .env file in same folder as this script, like:
# ipinfo-api-token="1234567890aabcdef"
#
load_dotenv()
access_token = os.environ.get("ipinfo-api-token")
handler = ipinfo.getHandler(access_token)

def get_ipinfo(ip_addy):
    details = handler.getDetails(ip_addy)
    return details
    
    
# Check format of IP Address
def standardize_ip(candidate):
    #IPv6 with a port - strip the port
    if "[" in candidate:
        candidate = candidate.split(']:')[0].replace("[","").replace("]","")

    try:
        ip = ipaddress.ip_address(candidate)
        ip = candidate
    except ValueError:
        #ipv4 with a port - strip the port
        ip = candidate.split(':')[0]
    return ip


# Begin Processing Inbound Logs
for file in files:
    df = pd.read_csv(file)

    for index, row in df.iterrows():
        audit_data_dict = json.loads(row['AuditData'])
        creation_time = audit_data_dict['CreationTime']
        user_id = audit_data_dict['UserId']
        
        if audit_data_dict.get('ClientIP'):
            client_ip = standardize_ip(audit_data_dict['ClientIP'])
        else:
            pass

        # Check Cache and Load if Missing
        if client_ip in cache:
            #print("hit")
            client_info = cache[client_ip]
            city = client_info['city']
            region = client_info['region']
            country_name = client_info['country_name']
        else:        
            #print("miss")
            if client_ip == "<null>":
                cache[client_ip] = { 'city': None, 'region': None, 'country_name': None }
                city = None
                region = None
                country_name = None
            else:    
                client_info = get_ipinfo(client_ip)
                try:
                    city = client_info.city
                except:
                    city = None
                    
                try:
                    region = client_info.region
                except:
                    region = None
                    
                try:
                    country_name = client_info.country_name
                except:
                    country_name = None
                    
                cache[client_ip] = {'city': city, 'region': region, 'country_name': country_name}
                
        results.append([creation_time, user_id, client_ip, city, region, country_name])        

  
# Convert List of Lists to Dataframe 
df = pd.DataFrame(results, columns = ['Creation Time', 'User Id', 'Client IP', 'City', 'Region', 'Country Name']) 


# Write to Outfile
df.to_excel(outfile, index=False)

