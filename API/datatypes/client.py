class Client:
    _id: int
    _client_name: str
    _contact_name: str
    _contact_phone: int # treated as bigint in db
    _billing_address_street_and_housenumber: str
    _billing_address_postal_code: str
    _billing_address_city: str
    _billing_address_state: str
    _billing_address_country: int

    def __init__(self, client_name, contact_name, contact_phone, billing_address_street_and_housenumber, billing_address_postal_code, billing_address_city, billing_address_state, billing_address_country, id = None):
        if id is not None:
            self._id = id
        else:
            self._id = None

        self._client_name = client_name
        self._contact_name = contact_name
        self._contact_phone = contact_phone
        self._billing_address_street_and_housenumber = billing_address_street_and_housenumber
        self._billing_address_postal_code = billing_address_postal_code
        self._billing_address_city = billing_address_city
        self._billing_address_state = billing_address_state
        self._billing_address_country = billing_address_country

    def getID(self):
        return self._id

    def getClientName(self):
        return self._client_name

    def getContactName(self):
        return self._contact_name

    def getContactPhone(self):
        return self._contact_phone

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
