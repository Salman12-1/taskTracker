import sys, json, os, datetime

FILENAME = "tasks.json"


def read_file():
    global FILENAME
    if not os.path.exists(FILENAME):
        return []
    
    with open(FILENAME, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError: # error raised whenever the module tries to parse text that isn't valid JSON
            return []

    return data

def write_file(data):
    global FILENAME
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=2)


def add_task(description):
    current_tasks = read_file()

    ID = len(current_tasks)
    #isoformat() used for datetime objects
    new_task = {"id":ID, "description":description, "status":"todo", "createdAt": datetime.datetime.today().isoformat(), "updatedAt": datetime.datetime.today().isoformat()}
    current_tasks.append(new_task)
    write_file(current_tasks)
    print("Task added successfully (ID: %d)\n"%ID)
    
def list_task():
    current_tasks = read_file()

    for task in current_tasks:
        print(f"""ID: {task["id"]}
Description: {task["description"]}
Status: {task["status"]}
Created At: {task["createdAt"]}
Updated At: {task["updatedAt"]}
""")
        
def update_task(id,description):
    current_tasks = read_file()

    for task in current_tasks:
        if task["id"] == id:
            task["description"] = description
            task["updatedAt"] = datetime.datetime.today().isoformat()
            write_file(current_tasks)
            return
    print("Task with ID: %d doesn't exist!"%id)

def delete_task(id):
    current_tasks = read_file()

    #use enumerate instead of manually tracking the index
    for index, task in enumerate(current_tasks):
        if task["id"] == id:
            current_tasks.pop(index)
            write_file(current_tasks)
            return
    print("Task with ID: %d doesn't exist!"%id)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: task_cli.py <command> [arguments]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: 'add' requires a description. Usage: add \"description\"")
        else:
            add_task(sys.argv[2])

    elif command == "list":
        list_task()

    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: 'update' requires an ID and a description. Usage: update <ID> \"description\"")
        else:
            update_task(int(sys.argv[2]), sys.argv[3])

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: 'delete' requires an ID. Usage: delete <id>")
        else:
            delete_task(int(sys.argv[2]))

