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
for local testing it will work. 

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
2. Install PostgreSQL on your computer. The exact steps vary depending on your
   operating system
    1. Linux - Debian (includes Ubuntu, Mint, etc.) 
     
       `sudo apt install postgresql-10`
    
    2. Linux - Fedora

       ```sudo dnf install postgresql```

    3. Mac OSX - There are a variety of ways to install PostgreSQL 10 on Mac 
       OSX. Please see the official [PostgreSQL Mac OSX download page][osx] 
       for instructions.
    4. Windows -




[epar]: https://evans.uw.edu/policy-impact/epar
[iqt]: http://v1008.host.s.uw.edu
[osx]: https://www.postgresql.org/download/macosx/