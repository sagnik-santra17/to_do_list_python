class Task:
    def __init__(self, task_name, task_category, task_description):
        self.task_name = task_name
        self.task_category = task_category
        self.task_description = task_description
        self.task_status = "Pending"
        self.task_creation_date = None
        self.task_due_date = None
        self.task_completion_date = None

    def to_dict(self):
        return {
                "task_name": self.task_name,
                "task_category": self.task_category,
                "task_description": self.task_description,
                "task_status": self.task_status,
                "task_due_date": self.task_due_date,
                "task_creation_date": self.task_creation_date,
                "task_completion_date": self.task_completion_date
            }
    

    def __str__(self):
        return f"Task name: {self.task_name}\nTask category: {self.task_category}\nDescription: {self.task_description}\nStatus: {self.task_status}\nTask creation date: {self.task_creation_date}\nDue date: {self.task_due_date}\nTask Completion date: {self.task_completion_date}"
