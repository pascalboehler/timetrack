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
from mysql.connector.utils import normalize_unicode_string

import os
from dotenv import load_dotenv
from pathlib import Path

# import custom datatypes
from datatypes.time_entry import TimeEntry
from datatypes.task import Task
from datatypes.client import Client
from datatypes.project import Project

# helper files
from logs import Log

class DatabaseHandler:

    connection: any
    database_connected: bool
    logger: Log

    def __init__(self, path):
        self.database_connected = False

        # init logger
        self.logger = Log("datebase_handler")

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
            self.logger.info(f"Database connection to {hostname} successful and working")
            return _connection
        except Error as err:
            self.logger.critical(err)

    def create_new_project(self, project: Project):
        query = f"""
        INSERT INTO project(title, client_id, hourly_rate, project_estimate, colour)
        VALUES (
            "{project.getTitle()}", {project.getClientID()}, {project.getHourlyRate()}, {project.getProjectEstimate()}, "{project.getColour()}");
        """ 
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            self.logger.info("New project created")
        except Error as err:
            self.logger.error(err)

    def delete_project(self, project: Project):
        if project.getID() is None:
            self.logger.warning("Couldn't delete project, ID was None")
            return
        
        query = f"""
        DELETE FROM project WHERE project_id={project.getID()};
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            self.logger.info(f"Project with ID {project.getID()} successfully deleted")
        except Error as err:
            self.logger.error(err)

    def read_project(self, project_id):
        query = f"""
        SELECT * FROM project WHERE project_id = {project_id};
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            list = []
            for result in results:
                list.append(result)

            dataset = list[0]
            project = Project(dataset[1], dataset[2], dataset[3], dataset[5], dataset[0], dataset[4])
            return project
        except Error as err:
            self.logger.error(err)

    def read_all_projects(self):
        query = """
        SELECT * FROM project
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            list = []
            for result in results:
                list.append(result)
            projects = []
            for dataset in list:
                project = Project(dataset[1], dataset[2], dataset[3], dataset[5], dataset[0], dataset[4])
                projects.append(project)
            return projects
        except Error as err:
            self.logger.error(err)

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
            self.logger.info("new client successfully created")
        except Error as err:
            self.logger.error(err)

    def delete_client(self, client: Client):
        if client.getID() is None:
            self.logger.warning("ClientID was None. Couldn't delete client")
            return

        query = f"DELETE FROM client WHERE client_id = {client.getID()}"
        cursor = self.connection.cursor()
        try:
            cursor.execure(query)
            self.connection.commit()
            self.logger.info(f"Client with ID {client.getID()} successfully deleted,")
        except Error as err:
            self.logger.error(err)

    def read_client(self, client_id):
        query = f"""
        SELECT * FROM client WHERE client_id = {client_id};
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            list = []
            for result in results:
                list.append(result)
            dataset = list[0]
            client = Client(dataset[1], dataset[2], dataset[3], dataset[4], dataset[5], dataset[6], dataset[7], dataset[8], dataset[9], dataset[0])
            return client
        except Error as err:
            self.logger.error(err)

    def read_all_clients(self):
        query = f"""
        SELECT * FROM client;
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            list = []
            for result in results:
                list.append(result)
            clients = []
            for dataset in list:
                client = Client(dataset[1], dataset[2], dataset[3], dataset[4], dataset[5], dataset[6], dataset[7], dataset[8], dataset[9], dataset[0])
                clients.append(client)
            return clients
        except Error as err:
            self.logger.error(err)

    def create_task(self, task: Task):
        query = f"""
        INSERT INTO task (task_name, project_id, task_hourly_rate)
        VALUES ("{task.getTaskName}", {task.getProjectID()}, {task.getTaskHourlyRate()});
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            self.logger.info("New task successfully created")
        except Error as err:
            self.logger.error(err)

    def delete_task(self, task: Task):
        if task.getID() is None:
            self.logger.warning("TaskID is None. Couldn't delete task")
            return

        query = f"""
        DELETE FROM task WHERE task_id = {task.getID()};
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            self.logger.info(f"Task with ID {task.getID()} successfully deleted")
        except Error as err:
            self.logger.error(err)

    def read_task(self, task_id):
        query = f"""
        SELECT * FROM task WHERE task_id = {task_id};
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            list = []
            for result in results:
                list.append(result)
            dataset = list[0]
            task = Task(dataset[1], dataset[2], dataset[3], dataset[0])
            return task
        except Error as err:
            self.logger.error(err)

    def read_all_tasks(self):
        query = f"""
        SELECT * FROM task;
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            list = []
            tasks = []
            for result in results:
                list.append(result)
            for dataset in list:
                task = Task(dataset[1], dataset[2], dataset[3], dataset[0])
                tasks.append(task)
            return tasks
        except Error as err:
            self.logger.error(err)

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
            self.logger.info("New  time entry successfully created")
        except Error as err:
            self.logger.error(err)

    def delete_time_entry(self, time_entry: TimeEntry):
        if time_entry.getID() is None:
            self.logger.warning("Time entry ID was None. Couldn't delete time entry")
            return
        
        query = f"""
        DELETE FROM time_entry WHERE entry_id={time_entry.getID()};
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            self.logger.info(f"Time entry with ID {time_entry.getID()} successfully created")
        except Error as err:
            self.logger.error(err)

    def read_time_entry(self, entry_id):
        query = f"""
        SELECT * FROM time_entry WHERE entry_id = {entry_id};
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            list = []
            for result in results:
                list.append(result)

            # get first dataset (query should only return 1 object!)
            dataset = list[0]
            time_entry = TimeEntry(
                dataset[1], dataset[2], dataset[3], dataset[4], dataset[5], dataset[6], dataset[7], dataset[8], dataset[9], dataset[0]
            )
            return time_entry
        except Error as err:
            self.logger.error(err)

    def read_all_time_entries(self):
        query = f"""
        SELECT * FROM time_entry;
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            list = []
            for result in results:
                list.append(result)
            time_entries = []
            for dataset in list:
                time_entry = TimeEntry(
                    dataset[1], dataset[2], dataset[3], dataset[4], dataset[5], dataset[6], dataset[7], dataset[8], dataset[9], dataset[0]
                )
                time_entries.append(time_entry)
            return time_entries
        except Error as err:
            self.logger.error(err)

if __name__ == "__main__":
    database = DatabaseHandler("./API/.env")

    print("--- TIME ENTRY ---")
    new_time_entry = database.read_time_entry(1)
    print(new_time_entry.getTitle())

    all_time_entries = database.read_all_time_entries()

    for entry in all_time_entries:
        print(entry.getTitle())

    print("--- TASK ---")

    new_task = database.read_task(1)
    print(new_task.getTaskName())

    all_tasks = database.read_all_tasks()

    for task in all_tasks:
        print(task.getTaskName())

    print("--- CLIENT ---")

    new_client = database.read_client(1)
    print(new_client.getClientName())

    all_clients = database.read_all_clients()

    for client in all_clients:
        print(client.getClientName())

    print("--- PROJECT ---")

    new_project = database.read_project(1)

    print(new_project.getTitle())

    all_projects = database.read_all_projects()

    for project in all_projects:
        print(project.getTitle())

