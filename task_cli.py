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


if __name__ == '__main__':
    command = sys.argv[1]

    if command == "add":
        add_task(sys.argv[2])

