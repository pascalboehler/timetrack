#
# database_handler.py
# Created on 09.12.2021
# Author: Pascal Boehler
# class for handling the database connection and reading writing to the database
#

###############
### Imports ###
###############
import mysql.connector
from mysql.connector import Error
from mysql.connector.utils import normalize_unicode_string

import os
from dotenv import load_dotenv
from pathlib import Path

'''
# import custom datatypes
from datatypes.time_entry import TimeEntry
from datatypes.task import Task
from datatypes.client import Client
from datatypes.project import Project
'''

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

    def write_to_db(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            self.logger.info(f"Succesfully stored data to DB")
        except Error as err:
            self.logger.error(err)

        