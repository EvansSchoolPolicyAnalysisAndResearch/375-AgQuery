#   [Evans School Policy Analysis and Research Group][epar]
##  Data Distribution Project

This repository was created to distribute the source code behind our  
[indicator query tool][iqt]. It was created using the  Flask Web Framework and
PostgreSQL 10. It was designed to be easily adaptable to similar projects
created by research teams around the world. Currently it is undergoing rapid
development as we strive to make it more user friendly and powerful. 

##  Getting Started: Setting Up A Dev Environment

If you are new to this project you can follow along with instructions below to
get set up with a working version of the website on your personal computer. If 
you are trying to set up a server using this code please make sure to follow
best industry practices. Setting up your server in this manner is insecure, but
for local testing it will work. If you wish to deploy this software on your
server please consult a professional.

These instructions assume you have some familiarity with the command line. 
While some of these steps may be completed using a graphic interface, many of 
them cannot. 
```
    Any instructions like this should be typed/pasted into your local terminal
```

### Steps:

1. Download a local copy of the code (clone the repository)
   
   Open up your terminal of choice and use the git command line tool to clone
   the repository. While you can use the GitHub desktop tool for this step, 
   later steps will require you to use the command line. 

   ```sh 
   git clone git@github.com:EvansSchoolPolicyAnalysisAndResearch/375-Ag-DB.git
   ```

2. Install/Setup Postgresql

   You will need to setup and install PostgreSQL. However, this is beyond 
   the scope of  this tutorial. Please see the following pages for operating
   system specific instructions. 

   1. Linux - [Debian (includes Ubuntu, Mint, etc.)][ubuntu]

   2. Linux - [Fedora Wiki][fedora]

   3. Mac OSX - [Postgress.app][osx]

   4. Windows

3. Setup the epardata Database within PostgreSQL.

   Once you have setup the PostgreSQL connect to it using the command line tool
   `psql`. How you do this will depend on your operating system but it should
   have been explained in the provided tutorial. 

   Once you have connected to the database run the following commands within
   the sql console to prepare the database for later. 
   ```sql
   -- Create the epardata user
   CREATE USER epardata PASSWORD '<password>';
   -- Create the 'epardata' database with the 'epardata' user as the owner.
   CREATE DATABASE epardata OWNER epardata;
   -- You're done, disconnect from the database
   \quit
   ```
7. Setup Python Virtual Environment.

   > With the exception of Windows, most operating systems come with a version
   > of Python installed. If you have python installed please check which 
   > version using `python --version`. If you are using python 3.6 or higher
   > you are all set. Some operating systems default to python 2.7. If this is
   > the case on your computer try typing `python3 --version` to check. If 
   > this is the case on your computer you will need to adjust when creating
   > a virtual environment (see below).

   Open a terminal within your downloaded repository 


[epar]: https://evans.uw.edu/policy-impact/epar
[iqt]: http://v1008.host.s.uw.edu
[ubuntu]: https://help.ubuntu.com/lts/serverguide/postgresql.html
[fedora]: https://fedoraproject.org/wiki/PostgreSQL
[osx]: https://postgresapp.com/
[win]: https://www.postgresql.org/download/windows/