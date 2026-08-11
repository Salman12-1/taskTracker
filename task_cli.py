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

    #to find the correct id value, handles case of task deleted, and empty list.
    ID = max((task["id"] for task in current_tasks), default = -1) + 1

    #isoformat() used for datetime objects
    new_task = {"id":ID, "description":description, "status":"todo", "createdAt": datetime.datetime.today().isoformat(), "updatedAt": datetime.datetime.today().isoformat()}
    current_tasks.append(new_task)
    write_file(current_tasks)
    print("Task added successfully (ID: %d)\n"%ID)
    
def list_task(status=""):
    current_tasks = read_file()

    for task in current_tasks:
        if status and task["status"] != status:
            continue
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


def mark_inProgress(id):
    current_tasks = read_file()

    for task in current_tasks:
        if task["id"] == id:
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.datetime.today().isoformat()
            write_file(current_tasks)
            return
        
    print("Task with ID: %d doesn't exists!"%id)

def mark_done(id):
    current_tasks = read_file()
    
    for task in current_tasks:
        if task["id"] == id:
            task["status"] = "done"
            task["updatedAt"] = datetime.datetime.today().isoformat()
            write_file(current_tasks)
            return
            
    print("Task with ID: %d doesn't exists!"%id)



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: task_cli.py <command> [arguments]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: 'add' requires a description. Usage: add \"description\"")
        else:
            #incase the user didn't use "" when adding the description.
            description = " ".join(sys.argv[2:])
            add_task(description)

    elif command == "list":
        if len(sys.argv) == 2:
            list_task()

        elif len(sys.argv) == 3:
            list_task(sys.argv[2])

        else: 
            print("Error: too many arguments!")


    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: 'update' requires an ID and a description. Usage: update <ID> \"description\"")
        else:
            #incase the user didn't use "" when adding the description.
            description = " ".join(sys.argv[3:])
            try:
                update_task(int(sys.argv[2]), description)
            except ValueError:
                print("Error: ID must be numeric")

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: 'delete' requires an ID. Usage: delete <ID>")

        elif len(sys.argv) > 3:
            print("Error: too many arguments!")

        else:
            try:
                delete_task(int(sys.argv[2]))
            except ValueError:
                print("Error: ID must be numeric")

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Error: 'mark-in-progress' requires an ID. Usage: mark-in-progress <ID>")

        elif len(sys.argv) > 3:
            print("Error: too many arguments!")

        else:
            try:
                mark_inProgress(int(sys.argv[2]))
            except ValueError:
                print("Error: ID must be numeric")

    elif command == "mark-done":
        if len(sys.argv) < 3:
                    print("Error: 'mark-done' requires an ID. Usage: mark-done <ID>")

        elif len(sys.argv) > 3:
            print("Error: too many arguments!")

        else:
            try:
                mark_done(int(sys.argv[2]))
            except ValueError:
                print("Error: ID must be numeric")

