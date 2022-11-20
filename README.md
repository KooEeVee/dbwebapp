# Graph Creator

## Overview
Graph Creator enables users to create info cards or simple graphs based on their data files in a web user interface.

Case: Oura data

## Features
- Create a user account
- Log in and log out
- Upload a file or files (csv or json) to the user account
- Pick the data fields for analysis
- Select an analysis tool for the data fields; for example a trend graph or monthly average value
- Select a time range for the data
- Update excisting data with new files

## To-do
Create a user account, log in and log out
* [x]users.py: [x]register user (username, password), [x]login, logout, session, [x]hash password, [x]username and password validation rules

Upload a file
* files.py: read file, inspect file and data, compare to the data rules (only numbers etc.), save validated data in a database, update data in the database

Analyse data
* analysis.py: select data from the database, operations for data analysis (date/time selection, calculate average), visualize data (draw a graph)

Templates
* [x]index.html
* [x]login.html
* [x]register.html
* data_tools.html
* dashboard.html
* [x]error.html
* logout.html

Database
* [x]db.py: database launch
* [x]schema.sql

Routes and app
* [x]routes.py: functions for page requests
* [x]app.py: application launch

Other files
* [x].gitignore
* [x].env
* requirements.txt

Layout
* CSS?
* Bootstrap?

Test Automation
* Robot Framework?
