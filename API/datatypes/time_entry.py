class TimeEntry:
    _title: str
    _date_begin: str
    _time_begin: str
    _date_end: str
    _time_end: str
    _project_id: int
    _client_id: int
    _task_id: int
    _billable: bool

    def __init__(self, title, date_begin, time_begin, date_end, time_end, client_id, project_id = None, task_id = None, billable = False):
        # init optional parameters if set otherwise set to default
        if project_id is not None:
            self._project_id = project_id
        else:
            self._project_id = 0;
        if task_id is not None:
            self._task_id = task_id
        else:
            self._task_id = 0
        if billable is not None:
            self._billable = billable
        else:
            self._billable = True
        
        self._title = title
        self._date_begin = date_begin
        self._time_begin = time_begin
        self._date_end = date_end
        self._time_end = time_end
        self._client_id = client_id
    
    def __str__(self):
        return f"{self._title}"

    def getTitle(self):
        return self._title

    def getDateBegin(self):
        return self._date_begin

    def getTimeBegin(self):
        return self._time_begin

    def getDateEnd(self):
        return self._date_end

    def getTimeEnd(self):
        return self._time_end

    def getClientID(self):
        return self._client_id

    def getTaskID(self):
        return self._task_id

    def getProjectID(self):
        return self._project_id

    def  getBillable(self):
        return self._billable