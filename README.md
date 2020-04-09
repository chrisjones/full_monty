# full_monty

This is a MO365 Log Parser inspired by https://github.com/nov3mb3r/monte-carlo.

### Install

1. Simply activate the Python environment

2. Install the dependencies with pip install -r requirements.txt

3. Execute python full_monty.py indir outdir

Where indir contains all of the MO365 logs for the investigation, and outdir is the output directory for the Excel file containing the following columns:

  - Creation Time
	- User Id
	- Client IP
	- City
	- Region
	- Country

The outdir is placed inside the indir directory to preserver organization if there anr multiple investigations ongoing.
