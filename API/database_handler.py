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

class Database_handler:

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

    def create_client(self, client_name, rate, contact_name, contact_phone, street, ptz, city, state, country):
        
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
            {client_name},
            {rate},
            {contact_name},
            {contact_phone},
            {street},
            {ptz},
            {city},
            {state},
            {country}
        )
        """

        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Client successfully created")
        except Error as err:
            print(f"Error '{err}'")

    def delete_client(self, client_id):
        query = f"DELETE FROM client WHERE client_id = {client_id}"
        cursor = self.connection.cursor()
        try:
            cursor.execure(query)
            self.connection.commit()
            print("Client deleted")
        except Error as err:
            print(f"Error '{err}'")


    def create_task(self, task_name, project_id, rate):
        query = f"""
        INSERT INTO task (task_name, project_id, task_hourly_rate)
        VALUES ("{task_name}", {project_id}, {rate});
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Task successfully created")
        except Error as err:
            print(f"Error '{err}'")

    def delete_task(self, task_id):
        query = f"""
        DELETE FROM task WHERE task_id = {task_id};
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Task deleted")
        except Error as err:
            print(f"Error '{err}'")





database = Database_handler("./.env")

#database.create_new_project("Super project", 1, 25.0, 2100.0, "blue")
#database.delete_project(3)


    