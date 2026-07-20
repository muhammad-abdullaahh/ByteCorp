class Task:
    def __init__(self, id, title, status="pending", due_date=None):
        self.id = id
        self.title = title
        self.status = status
        self.due_date = due_date

    def __str__(self):
        return f"[{self.id}] {self.title} | Status: {self.status} | Due: {self.due_date}"

    def __repr__(self):
        return self.__str__()