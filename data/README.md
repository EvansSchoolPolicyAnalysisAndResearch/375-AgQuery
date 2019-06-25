# Database Updater

The scripts in this folder update the data in the [ADIQuT][iqt] Database. They
are designed to pull the latest version of the data from [EPAR's][epar] 
Agricultural Data Curation Project. More information on the project is available
[on our website][curation], and the data is hosted on [EPAR's Github
Page][datadis]. 

The primary script is `db_updater.py` which relies on `update-database.sql`. 
Between these two scripts the spreadsheet is downloaded from the 335 Data 
Dissemination GitHub repository, the data is extracted, cleaned, and saved to
CSV. These CSVs are then used by `update-database.sql` to update the data in the
ADIQuT database.

## Usage Directions

Typing `db_updater.py -h` at the console will display the help file.

### Fully Automated Database Update

When `db_updater.py` is run from the command line with no further arguments the
full database update will be performed with little further assistance needed 
from the user. You will need to enter the database password, but the rest is 
handled automatically. If you wish to update the database without having to 
enter the password, please see the PostgreSQL [password file
documentation][pgpass] and set up a `~/.pgpass` file.

### Running Pieces of the Script

Using `db_updater.py` you can emulate the previous 3 script system which -
`excel_extractor.py`, `estimates_cleaner.py`, and `construction_cleaner.py` -
with  specific command line flags.

- `db_updater.py -x <NAME OF EXCEL WORKBOOK>` Running the script with the `-x` 
parameter will extract the the relevant sheets from a pre-downloaded version of
the EPAR 335 spreadsheet and save them as estimates.csv and decs.csv for the
indicator estimates and indicator construction decision sheets respectively.

- `db_updater.py -c <CONSTRUCTION DECISIONS CSV>` Running the script with the 
`-c` parameter will clean the provided construction decisions csv extracted from
the Excel workbook. It will output to decs_cleaned.csv for the
crosswave information and ctry_decs_cleaned.csv for the country specific
information.

- `db_updater.py -e <ESTIMATES CSV>` Running the script with the `-e` parameter
    will clean the provided indicator estimates csv extracted from the Excel
    workbook. It will output to estimates_cleaned.csv.


[iqt]:      http://v1008.host.s.uw.edu
[epar]:     https://evans.uw.edu/policy-impact/epar
[curation]: https://evans.uw.edu/policy-impact/epar/agricultural-development-data-curation
[datadis]:  https://github.com/EvansSchoolPolicyAnalysisAndResearch/335_Data-Dissemination
[pgpass]:   https://www.postgresql.org/docs/10/libpq-pgpass.html