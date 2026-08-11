Task Tracker CLI
A simple command-line application to track and manage your tasks. Tasks are stored locally in a tasks.json file, so your data persists between runs.

Getting Started:
1. Clone this repository or download task_cli.py.
2. Open a terminal in the project folder.
3. Run commands using the format below.
   

py task_cli.py (command) [arguments]

A tasks.json file will be created automatically in the same folder the first time you add a task.



Commands


Add a task:

   py task_cli.py add "Buy groceries"


Update a task's description:

   py task_cli.py update 0 "Buy groceries and cook dinner"


Delete a task:

   py task_cli.py delete 0


Mark a task as in progress:

   py task_cli.py mark-in-progress 0


Mark a task as done:

   py task_cli.py mark-done 0


List all tasks:

   py task_cli.py list


List tasks by status:

   py task_cli.py list done

   py task_cli.py list todo

   py task_cli.py list in-progress



Notes:

Task descriptions with spaces don't need to be wrapped in quotes — the CLI will join multiple words automatically. Quoting is still recommended for clarity.

If you run a command with missing or too many arguments, the CLI will print a usage message instead of crashing.
