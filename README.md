# Graph Creator

## Overview
Graph Creator enables users to create info cards or simple graphs based on their data files in a web user interface.

Case: Oura data

## Features
- Create a user account
- Log in and log out
- Upload a file or files (csv) to the user account
- Pick the data fields for analysis
- Select an analysis tool for the data fields; for example a trend graph or monthly average value
- Select a time range for the data
- Update excisting data with new files

## To-do
Create a user account, log in and log out
* [x]users.py: [x]register user (username, password), [x]login, [x]logout, [x]session, [x]hash password, [x]username and [x]password validation rules

Upload a file
* files.py: [x]upload csv file, save csv data in a table[x], show uploaded files on the user dashboard[x], show preview table of uploaded files on the user dashboard, file validation rules, read file, inspect file and data, compare to the data rules (only numbers etc.), update data in the database (replace)[x], update data in the database (append)

Analyse data
* analyse.py: select data from the database, operations for data analysis (date/time selection, calculate average), visualize data (draw a graph)

Templates
* [x]index.html
* [x]login.html
* [x]register.html
* [x]files_upload.html
* [x]files_update.html
* [x]tools.html
* [x]dashboard.html
* [x]error.html
* [x]logout.html

Database
* [x]db.py: database connection launch
* [x]schema.sql

Routes and app
* [x]routes.py: functions for page requests
* [x]app.py: application launch

Other files
* [x].gitignore
* [x].env
* [x]requirements.txt

Layout
* CSS?
* Bootstrap?

Test Automation
* Robot Framework?
