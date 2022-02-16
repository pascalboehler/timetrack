#
# client.py
# Created on 10.12.2021
# Author: Pascal Boehler
# client class for savely working with the client object
#

from API.database_classes.database_handler import DatabaseHandler


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

    ##########################
    ### Database functions ###
    ##########################

    def fetch(self, db):
        # function for fetching changes made to the specific object before manipulating it
        query = f"""SELECT * FROM client WHERE client_id = {self._id}"""

        print("FETCH")

    def store(self, db: DatabaseHandler):
        if self._id is None:
           self. _create(db=db)
        else:
            self._update()

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
            {self._client_name},
            {self._contact_name},
            {self._contact_name}
            {self._hourly_rate},
            {self._billing_address_street_and_housenumber},
            {self._billing_address_postal_code},
            {self._billing_address_city},
            {self._billing_address_state},
            {self._billing_address_country}
        )
        """

        db.write_to_db(query)

        print("CREATE")

    def _update(self, db):
        print("UPDATE")

    def edit():
        print("Client xyz updated")

    def delete():
        print("DELETED")
