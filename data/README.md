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


[iqt]:      http://v1008.host.s.uw.edu
[epar]:     https://evans.uw.edu/policy-impact/epar
[curation]: https://evans.uw.edu/policy-impact/epar/agricultural-development-data-curation
[datadis]:  https://github.com/EvansSchoolPolicyAnalysisAndResearch/335_Data-Dissemination