class Task:
    _id: str
    _task_name: str
    _project_id: int
    _task_hourly_rate: float

    def __init__(self, task_name, project_id, task_hourly_rate, id = None):
        if id is not None:
            self._id = id
        else:
            self._id = None

        self._task_name = task_name
        self._project_id = project_id
        self._task_hourly_rate = task_hourly_rate

    def getID(self):
        return self._id

    def getTaskName(self):
        return self._task_name

    def getID(self):
        return self._id

    def getProjectID(self):
        return self._project_id

    def getTaskHourlyRate(self):
        return self._task_hourly_rate
