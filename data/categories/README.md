# Indicator Categorization Tool

The indicator categorization tool was designed to put indicators into categories
based on the available disaggregations. The tool itself is written in python 
and can be run using `python ict.py`. Running the tool outputs markdown 
formatted text to the terminal. In combination with `mdMemo.latex` and 
`meta.yaml` the output can be turned into a pdf using [pandoc][pandoc]. This process has been automated with make. running `make all` from the commandline
will run the tool and automatically output the results into a memo named
`indicator-categories.pdf`. This process requires the user to have pandoc
installed along with lualatex (default) or xelatex - modifiable in the the 
makefile. If you instead type `make md` the markdown file used to generate the
pdf will be output to `indicator-categories.md`

[agq]:      https://www.agquery.org
[epar]:     https://evans.uw.edu/policy-impact/epar
[curation]: https://evans.uw.edu/policy-impact/epar/agricultural-development-data-curation
[datadis]:  https://github.com/EvansSchoolPolicyAnalysisAndResearch/335_Data-Dissemination
[pandoc]:	https://pandoc.org/
[pgpass]:   https://www.postgresql.org/docs/10/libpq-pgpass.html
