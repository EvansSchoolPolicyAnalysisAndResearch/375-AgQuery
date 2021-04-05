# Database Updater

The scripts in this folder update the data in the [AgQuery][agq] Database. They
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

Typing `./db_updater.py -h` at the console will display the help file.

### Fully Automated Database Update

When `./db_updater.py` is run from the command line with no further arguments
the full database update will be performed with little further assistance
needed from the user. You will need to enter the database password, but the
rest is handled automatically. If you wish to update the database without
having to enter the password, please see the PostgreSQL [password file
documentation][pgpass] and set up a `~/.pgpass` file.

[agq]:      https://www.agquery.org
[epar]:     https://evans.uw.edu/policy-impact/epar
[curation]: https://evans.uw.edu/policy-impact/epar/agricultural-development-data-curation
[datadis]:  https://github.com/EvansSchoolPolicyAnalysisAndResearch/335_Data-Dissemination
[pgpass]:   https://www.postgresql.org/docs/10/libpq-pgpass.html
