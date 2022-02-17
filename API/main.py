from database_classes.database_handler import DatabaseHandler
from datatypes.client import Client
def main():
    test_client_write_db()

def testDB():
    database = DatabaseHandler("./API/.env")

    print("--- TIME ENTRY ---")
    new_time_entry = database.read_time_entry(1)
    print(new_time_entry.getTitle())

    all_time_entries = database.read_all_time_entries()

    for entry in all_time_entries:
        print(entry.getTitle())

    print("--- TASK ---")

    new_task = database.read_task(1)
    print(new_task.getTaskName())

    all_tasks = database.read_all_tasks()

    for task in all_tasks:
        print(task.getTaskName())

    print("--- CLIENT ---")

    new_client = database.read_client(1)
    print(new_client.getClientName())

    all_clients = database.read_all_clients()

    for client in all_clients:
        print(client.getClientName())

    print("--- PROJECT ---")

    new_project = database.read_project(1)

    print(new_project.getTitle())

    all_projects = database.read_all_projects()

    for project in all_projects:
        print(project.getTitle())

def test_client_write_db():

    # create a new client
    client = Client("test", "Test", 12345, 42.3, "Teststrasse 1", "123456", "Frankfurt", "HESSE", "Germany")
    db = DatabaseHandler("./.env")

    client.store(db)

    client.setClientName("Bernd")

    client.store(db)

    client.fetch(db)
    
    print("TESTED")

if __name__ == "__main__":
    main()
