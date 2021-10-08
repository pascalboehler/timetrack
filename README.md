# TimeTrack

## The idea

As part of my job, I am forced to track the time I work and send a monthly report back to the company. Additionally, I sometimes have to extract certain projects of that time tracker to send invoices to clients. Because I haven't found a great tool do this for me and maybe also sync to my calendar, I want to build it on my own, making sure it includes every feature I need it to include. This software is also meant to stay 100% open source and free of charge, so everyone is able to use it and can contribute to the project.

## List of features / Requirements for the tool

- Insert hours worked into a database
- for every entry being able to store:
    - hours worked
    - date
    - start time
    - end time
    - Title / Work description
    - Project
    - Client
    - Task (like editing, shooting, preparation etc.)
    - tag if billable or not
- for every project being able to store:
    - **project_ID**
    - project title
    - client the project belongs to (via **client_ID**)
    - hourly rate
    - *project estimate* (budget or time)
    - *colour* (for easier spotting)
- for every client being able to store:
    - **client_ID**
    - client name
    - name of contact person
    - billing address
    - default hourly rate (which will be overwritten by project)
- create time entries manually (by entering required information)
- create time entries via stopclock
- automate time creation, eg. when Program X is opened, start tracking for project Y.
- export project overview / reports as PDF via LaTex
- export invoices for client as PDF via LaTex (on specific project / time frame)
- being able to import owm LaTex templates for reports and invoices -> keep a consistent corp design
- access the service via web, phone and desktop app / cmd (Win & Mac)
- being able to easily host own instance on own infrastructure (like corp server, NAS whatever)
- display overview of past month etc.
- sync with google calendar => being able to copy cal entry as time entry including title etc.
- show estimate earning for week / month / year by including planned work assignments from calendar
- be able to develop own frontend for backend solution => write to DB via REST Api

## Tasks
[] Create database scheme 
