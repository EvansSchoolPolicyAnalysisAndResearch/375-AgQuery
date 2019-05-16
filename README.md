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
   ```sh 
   git clone git@github.com:EvansSchoolPolicyAnalysisAndResearch/375-Ag-DB.git
   ```

2. You will need to setup and install PostgreSQL. However, this is beyond 
   the scope of  this tutorial. Please see the following pages for operating
   system specific instructions. 

   1. Linux - Debian (includes Ubuntu, Mint, etc.)

   2. Linux - Fedora

   3. Mac OSX

   4. Windows

3. Once you have setup the database connect to it using the command line tool
   `psql`. How you do this will depend on your operating system but it should
   have been explained in the provided tutorial. 
4. Create the `epardata` user replace `<password>` with your password
   
   ```sql
   CREATE ROLE epardata PASSWORD '<password>';
   ```

5. Create the `epardata` database with `epardata` as the owner
   ```sql
   CREATE DATABASE epardata OWNER epardata;
   ```
6. 


[epar]: https://evans.uw.edu/policy-impact/epar
[iqt]: http://v1008.host.s.uw.edu
[osx]: https://www.postgresql.org/download/macosx/
[win]: https://www.postgresql.org/download/windows/