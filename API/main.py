import database_classes.database_handler as DB_Handler

def main():
    testDB()

def testDB():
    database = DB_Handler.DatabaseHandler("./API/.env")

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

if __name__ == "__main__":
    main()
