#
# database_handler.py
# Created on 09.12.2021
# Author: Pascal Boehler
# class for handling the database connection and reading writing to the database
#

###############
### Imports ###
###############
from typing import Any
import mysql.connector
from mysql.connector import Error

import os
from dotenv import load_dotenv
from pathlib import Path

# import custom datatypes
from datatypes.time_entry import TimeEntry
from datatypes.task import Task
from datatypes.client import Client

class DatabaseHandler:

    connection: any
    database_connected: bool

    def __init__(self, path):
        self.database_connected = False

        # load database credentials from .env file
        dotenv_path = Path(path)
        load_dotenv(dotenv_path=dotenv_path)
        hostname = os.getenv('DB_HOSTNAME')
        username = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWD')
        database = os.getenv('DB_DATABASE')

        self.connection = self.create_database_connection(hostname, username, password, database)

    def create_database_connection(self, hostname, username, password, database_name):
        try:
            _connection = mysql.connector.connect(
                host = hostname,
                user = username,
                passwd = password,
                database = database_name
            )
            self.database_connected = True;
            print("Connection successful and working!")
            return _connection
        except Error as err:
            print(f"Error: '{err}'")

    def create_new_project(self, project_title, client_id, hourly_rate, project_estimate, colour):
        query = f"""
        INSERT INTO project(title, client_id, hourly_rate, project_estimate, colour)
        VALUES (
            "{project_title}", {client_id}, {hourly_rate}, {project_estimate}, "{colour}");
        """ 
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Project created!")
        except Error as err:
            print(f"Error '{err}'")

    def delete_project(self, project_id):
        query = f"""
        DELETE FROM project WHERE project_id={project_id};
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Project deleted")
        except Error as err:
            print(f"Error '{err}'")

    def create_client(self, client: Client):
        
        # Function for creating a new client entry in the database

        query = f"""
        INSERT INTO client (
            client_name,
            contact_name,
            contact_phone,
            default_hourly_rate,
            billing_address_street_and_housenumber,
            billing_address_postal_code,
            billing_address_city,
            billing_address_state,
            billing_address_country
        )
        VALUES (
            {client.getClientName()},
            {client.getContactName()},
            {client.getContactPhone()}
            {client.getHourlyRate()},
            {client.getBillingAddressStreetAndHousenumber()},
            {client.getBillingAddressPostalCode()},
            {client.getBillingAddressCity()},
            {client.getBillingAddressState()},
            {client.getBillingAddressCountry()}
        )
        """

        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Client successfully created")
        except Error as err:
            print(f"Error '{err}'")

    def delete_client(self, client: Client):
        query = f"DELETE FROM client WHERE client_id = {client.getID()}"
        cursor = self.connection.cursor()
        try:
            cursor.execure(query)
            self.connection.commit()
            print("Client deleted")
        except Error as err:
            print(f"Error '{err}'")


    def create_task(self, task: Task):
        query = f"""
        INSERT INTO task (task_name, project_id, task_hourly_rate)
        VALUES ("{task.getTaskName}", {task.getProjectID()}, {task.getTaskHourlyRate()});
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Task successfully created")
        except Error as err:
            print(f"Error '{err}'")

    def delete_task(self, task: Task):
        query = f"""
        DELETE FROM task WHERE task_id = {task.getID()};
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Task deleted")
        except Error as err:
            print(f"Error '{err}'")

    def create_time_entry(self, time_entry: TimeEntry):
        query = f"""
        INSERT INTO time_entry (
            title,
            date_begin,
            time_begin,
            date_end,
            time_end,
            project_id,
            client_id,
            task_id,
            billable
        )
        VALUES (
            "{time_entry.getTitle()}",
            "{time_entry.getDateBegin()}",
            "{time_entry.getTimeBegin()}",
            "{time_entry.getDateEnd()}",
            "{time_entry.getTimeEnd()}",
            {time_entry.getClientID()},
            {time_entry.getTaskID()},
            {time_entry.getProjectID()},
            {time_entry.getBillable()}
        );
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Time entry created successfully")
        except Error as err:
            print(f"Error '{err}")


database = DatabaseHandler("./API/.env")

time_entry = TimeEntry("Test", "2022-09-09", "22:22:22", "2022-09-09", "23:59:59", 1, 1, 1, True)

database.create_time_entry(time_entry)

#database.create_new_project("Super project", 1, 25.0, 2100.0, "blue")
#database.delete_project(3)