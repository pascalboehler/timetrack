#
# client.py
# Created on 10.12.2021
# Author: Pascal Boehler
# client class for savely working with the client object
#

from database_classes.database_handler import DatabaseHandler
from logs import Log

class Client:
    _id: int
    _client_name: str
    _contact_name: str
    _contact_phone: int # treated as bigint in db
    _hourly_rate: float
    _billing_address_street_and_housenumber: str
    _billing_address_postal_code: str
    _billing_address_city: str
    _billing_address_state: str
    _billing_address_country: int
    _logger: Log

    def __init__(self, client_name, contact_name, contact_phone, hourly_rate, billing_address_street_and_housenumber, billing_address_postal_code, billing_address_city, billing_address_state, billing_address_country, id = None):
        if id is not None:
            self._id = id
        else:
            self._id = None

        self._client_name = client_name
        self._contact_name = contact_name
        self._contact_phone = contact_phone
        self._hourly_rate = hourly_rate
        self._billing_address_street_and_housenumber = billing_address_street_and_housenumber
        self._billing_address_postal_code = billing_address_postal_code
        self._billing_address_city = billing_address_city
        self._billing_address_state = billing_address_state
        self._billing_address_country = billing_address_country

        self._logger = Log("client")

    ###########################
    ### GETTERS AND SETTERS ###
    ###########################
    def getID(self):
        return self._id

    def getClientName(self):
        return self._client_name

    def getContactName(self):
        return self._contact_name

    def getContactPhone(self):
        return self._contact_phone

    def getHourlyRate(self):
        return self._hourly_rate

    def getBillingAddressStreetAndHousenumber(self):
        return self._billing_address_street_and_housenumber

    def getBillingAddressPostalCode(self):
        return self._billing_address_postal_code

    def getBillingAddressCity(self):
        return self._billing_address_city

    def getBillingAddressState(self):
        return self._billing_address_state

    def getBillingAddressCountry(self):
        return self._billing_address_country

    def setClientName(self, name):
        self._client_name = name

    ##########################
    ### Database functions ###
    ##########################

    def fetch(self, db):
        # function for fetching changes made to the specific object before manipulating it
        query = f"""SELECT * FROM client WHERE client_id = {self._id}"""

        data = db.read_from_db(query)

        print(data)

    def store(self, db: DatabaseHandler):
        if self._id is None:
           self._create(db=db)
        else:
            self._update(db=db)

    def _create(self, db: DatabaseHandler):
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
            '{self._client_name}',
            '{self._contact_name}',
            {self._contact_phone},
            {self._hourly_rate},
            '{self._billing_address_street_and_housenumber}',
            '{self._billing_address_postal_code}',
            '{self._billing_address_city}',
            '{self._billing_address_state}',
            '{self._billing_address_country}'
        );
        SELECT LAST_INSERT_ID() AS client_id;
        """

        result = db.create_object(query)

        self._id = result
        self._logger.info(f"Successfully created client with ID {self._id}")

    def _update(self, db: DatabaseHandler):
        query = f"""
        UPDATE client
        SET
            client_name = "{self._client_name}", 
            contact_name = "{self._contact_name}",
            contact_phone = {self._contact_phone},
            default_hourly_rate = {self._hourly_rate},
            billing_address_street_and_housenumber = "{self._billing_address_street_and_housenumber}",
            billing_address_postal_code = "{self._billing_address_postal_code}",
            billing_address_city = "{self._billing_address_city}",
            billing_address_state = "{self._billing_address_state}",
            billing_address_country = "{self._billing_address_country}"
        WHERE
            client_id = {self._id}
        """

        db.write_to_db(query)

        self._logger.info(f"Successfully updated client with ID {self._id}")

    def delete(self, db: DatabaseHandler):
        query = f"""
        DELETE FROM client WHERE client_id = {self._id};
        """

        db.delete_from_db(query)

        self._id = None # mark object as not stored in DB!!

        self._logger.info(f"Successfully deleted client from database")
