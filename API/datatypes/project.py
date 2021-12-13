class Project:
    _id: int
    _title: str
    _client_id: str
    _hourly_rate: float
    _project_estimate: float
    _colour: str
    
    def __init__(self, title, client_id, hourly_rate, colour, id = None, project_estimate = None):
        if id is not None:
            self._id = id
        else:
            self._id = None

        if project_estimate is not None:
            self._project_estimate = project_estimate
        else:
            self._project_estimate = 0.0

        self._title = title
        self._client_id = client_id
        self._hourly_rate = hourly_rate
        self.colour = colour

    def getID(self):
        return self._id

    def getTitle(self):
        return self._title

    def getClientID(self):
        return self._client_id

    def getHourlyRate(self):
        return self._hourly_rate

    def getProjectEstimate(self):
        return self._project_estimate

    def getColour(self):
        return self._colour