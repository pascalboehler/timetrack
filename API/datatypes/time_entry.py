class TimeEntry:
    title: str
    date_begin: str
    time_begin: str
    date_end: str
    time_end: str
    project_id: int
    client_id: int
    task_id: int
    billable: bool

    def __init__(self, title, date_begin, time_begin, date_end, time_end, client_id, project_id = None, task_id = None, billable = False):
        # init optional parameters if set otherwise set to default
        if project_id is not None:
            self.project_id = project_id
        else:
            self.project_id = 0;
        if task_id is not None:
            self.task_id = task_id
        else:
            self.task_id = 0
        if billable is not None:
            self.billable = billable
        else:
            self.billable = True
        
        self.title = title
        self.date_begin = date_begin
        self.time_begin = time_begin
        self.date_end = date_end
        self.time_end = time_end
        self.client_id = client_id
    
    def __str__(self):
        return f"{self.title}"