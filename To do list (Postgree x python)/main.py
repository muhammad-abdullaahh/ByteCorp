from db.database import Database
from repository.task_repository import TaskRepository
from cli.cli import TaskManagerCLI

def main():
    database = Database()
    repository = TaskRepository(database)
    cli = TaskManagerCLI(repository)
    cli.run()

if __name__ == "__main__":
    main()