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

The [outdir] is placed inside the [indir] directory to preserver organization if there are multiple investigations ongoing.

## Further Information

### ipinfo.io

This script makes use of https://ipinfo.io.  There is a free signup that allows for 50,000 lookups per month.  Simply signup and copy your API token.


### dotenv

This script also makes use of dotenv to store the API key so it doesn't get saved is source control.  Create a file named .env in the same directory as this script and enter this line replacing the sample token with your token:

   ```
   ipinfo-api-token='1234567890abcdef' 
   ```

## Contributions

I highly encourage contributors to send in any and all pull requests or issues. 