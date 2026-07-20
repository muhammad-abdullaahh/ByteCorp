from models.task import Task

class TaskRepository:
    def __init__(self, database):
        self.database = database

    def add_task(self, title, due_date):
        conn = self.database.connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO tasks (title, due_date) VALUES (%s, %s) RETURNING id, status",
            (title, due_date)
        )
        result = cur.fetchone()
        conn.commit()
        cur.close()
        self.database.close()
        return Task(id=result[0], title=title, status=result[1], due_date=due_date)

    def get_all_tasks(self):
        conn = self.database.connect()
        cur = conn.cursor()
        cur.execute("SELECT id, title, status, due_date FROM tasks ORDER BY id")
        rows = cur.fetchall()
        cur.close()
        self.database.close()
        return [Task(id=r[0], title=r[1], status=r[2], due_date=r[3]) for r in rows]

    def get_tasks_by_status(self, status):
        conn = self.database.connect()
        cur = conn.cursor()
        cur.execute("SELECT id, title, status, due_date FROM tasks WHERE status = %s ORDER BY id", (status,))
        rows = cur.fetchall()
        cur.close()
        self.database.close()
        return [Task(id=r[0], title=r[1], status=r[2], due_date=r[3]) for r in rows]

    def update_task_status(self, task_id, new_status):
        conn = self.database.connect()
        cur = conn.cursor()
        cur.execute("UPDATE tasks SET status = %s WHERE id = %s", (new_status, task_id))
        updated = cur.rowcount > 0
        conn.commit()
        cur.close()
        self.database.close()
        return updated

    def delete_task(self, task_id):
        conn = self.database.connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        deleted = cur.rowcount > 0
        conn.commit()
        cur.close()
        self.database.close()
        return deleted