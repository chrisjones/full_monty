# full_monty

This is a MO365 Log Parser inspired by https://github.com/nov3mb3r/monte-carlo. And because I like bad British comedy.

## Install

1. Create and Activate the Python environment: 

   ```
   python -m venv env
   ```

   ```
   env/bin/activate
   ```

2. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Execute:

   ```
   python full_monty.py [indir] [outdir]
   ```

Where [indir] contains all of the MO365 logs for the investigation, and [outdir] is the output directory for the Excel file containing the following columns:

  - Creation Time
  - User Id
  - Client IP
  - City
  - Region
  - Country

The [outdir] is placed inside the [indir] directory to preserve organization if there are multiple investigations ongoing.

## Further Information

### ipinfo.io

This script makes use of https://ipinfo.io.  There is a free signup that allows for 50,000 lookups per month.  Simply signup and copy your API token.


Additional details may be obtained from ipinfo (see below); however, the current script only collects the City, State or Region, and Country Name.


    >>> import pprint
    >>> pprint.pprint(details.all)
	 {'abuse': {'address': 'US, CA, Mountain View, 1600 Amphitheatre Parkway, 94043',
	            'country': 'US',
	            'email': 'network-abuse@google.com',
	            'name': 'Abuse',
	            'network': '216.239.32.0/19',
	            'phone': '+1-650-253-0000'},
	  'asn': {'asn': 'AS15169',
	          'domain': 'google.com',
	          'name': 'Google LLC',
	          'route': '216.239.36.0/24',
	          'type': 'business'},
	  'city': 'Mountain View',
	  'company': {'domain': 'google.com', 'name': 'Google LLC', 'type': 'business'},
	  'country': 'US',
	  'country_name': 'United States',
	  'hosting': {'host': 'google',
	              'id': 'GOOGLE',
	              'name': 'Google LLC',
	              'network': '216.239.32.0/19'},
	  'hostname': 'any-in-2415.1e100.net',
	  'ip': '216.239.36.21',
	  'latitude': '37.3861',
	  'loc': '37.3861,-122.0840',
	  'longitude': '-122.0840',
	  'postal': '94035',
	  'region': 'California',
	  'timezone': 'America/Los_Angeles'}



### dotenv

This script also makes use of dotenv to store the API key so it doesn't get saved is source control.  Create a file named .env in the same directory as this script and enter this line replacing the sample token with your token:

   ```
   ipinfo-api-token='1234567890abcdef' 
   ```

## Contributions

I highly encourage contributors to send in any and all pull requests or issues. 

### License

GPLv3