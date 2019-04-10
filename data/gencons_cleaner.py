#data/gencons_cleaner
import csv
import re
# Clean the gencons file
with open('gencons.csv', newline='') as infile:
	with open('gencons_cleaned.csv', 'w', newline='') as outfile:
		rdr = csv.reader(infile, delimiter=',', quotechar='"', 
			quoting=csv.QUOTE_NONNUMERIC)
		wrtr = csv.writer(outfile, delimiter=',', quotechar='"', 
			quoting=csv.QUOTE_NONNUMERIC)
		for r,row in enumerate(rdr):
			# Postgres does not like having headers, so this removes them
			if r == 0:
				row[0] = "Intro"
				row[1] = """
The data on this site were curated by the [Evans Policy Analysis and Research Group](https://evans.uw.edu/policy-impact/epar) (EPAR) at the [Daniel J. Evans School of Public Policy and Governance](https://evans.uw.edu/) of the [University of Washington](https://uw.edu). The raw data were collected as part of the [LSMS-ISA](http://surveys.worldbank.org/lsms/programs/integrated-surveys-agriculture-ISA) conducted by the [World Bank Group](http://www.worldbank.org/) and can be downloaded from their site.

For each country the data were collected by the respective country's Statistical Bureau. For more information on each survey and to download the data see the following links:

- [Ethiopa Socioeconomic Survey (ESS)](http://surveys.worldbank.org/lsms/programs/integrated-surveys-agriculture-ISA/ethiopia)
- [Nigeria General Household Survey Panel (GHSP)](http://surveys.worldbank.org/lsms/programs/integrated-surveys-agriculture-ISA/nigeria)
- [Tanzania National Panel Survey (TNPS)](http://surveys.worldbank.org/lsms/programs/integrated-surveys-agriculture-ISA/tanzania)

The data were curated using the [STATA](https://www.stata.com/) software package. The STATA source code files used to curate the data can be found on [Github](https://github.com) in [EPAR's repositories](https://github.com/EvansSchoolPolicyAnalysisAndResearch/335_Agricultural-Indicator-Curation). These files, along with the data from the World Bank's site can be used to recreate these estimates. General decision rules for this curation are detailed below."""
				wrtr.writerow(row)
				continue
			# A single carriage return needs to be replaced with two to mark 
			# a new paragraph in markdown
			row[1] = row[1].replace("\n", "\n\n")
			# Finds lists of the format (digit) and replaces them with the
			# markdown standard [digit]. format
			row[1] = re.sub(r'^\s*\(([0-9]+)\)', r'\1.', row[1], flags=re.MULTILINE)
			# Turns the bullets used in the excel spread sheet into markdown
			# unordered list elements.
			row[1] = re.sub(r'\n(\s*)[•]', r'\1-', row[1], flags=re.MULTILINE)
			# Searches for headers in the document and makes them markdown h3
			row[1] = re.sub(r'^\s*?[^-]([ a-zA-Z0-9]*?):[\s]*$', r'\n### \1:', row[1], flags=re.MULTILINE)
			# Write the cleaned row to the cleaned file
			wrtr.writerow(row)