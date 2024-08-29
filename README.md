# Task Manager CLI Tool

Welcome to my Task Manager CLI tool! This simple command-line application helps to manage the tasks efficiently. We can add, view, complete, and delete tasks using this tool. All tasks are stored in a text file called `tasks.txt`.

## Features

- **Add Tasks:** Quickly add multiple tasks with a single input.
- **View Tasks:** List all your tasks with their current status.
- **Complete Tasks:** Mark tasks as completed once they are done.
- **Delete Tasks:** Remove tasks that are no longer needed.


**Functions**

### `load_tasks()`

**Purpose:**  

Loads all tasks from the `tasks.txt` file into a list.

**Functionality:**  

- Checks if the `tasks.txt` file exists. If it does not exist - returns an empty list.
- Check the contents of the file, removing leading/trailing whitespace from each line.
- Returns the list of tasks.

### `save_tasks(tasks)`

**Purpose:**  

Saves the list of tasks to the `tasks.txt` file.

**Functionality:**
- Opens the file `tasks.txt` in write mode.
 - Writes all the tasks available from the given list to the file, where each task goes on a new line.

### `add_task(task_descriptions)`

**Purpose:**  
Appends one or many new tasks to the list with status `[Pending]`.

**Functionality:**  
- Accepts a comma-separated string of descriptions of the tasks to be written.
- Splits the input into individual tasks, the outputted string would then look like this:.
- Checks that no new task does not appear twice
- Adds each task to the list with its status marked as `[Pending]`.
- Overwrites the `tasks.txt` file with the new list of tasks.

### `list_tasks()`

**Purpose:** 

To view all tasks along with their status.

**Functionality:** 

- Outputs the current task list.
- Outputs every task within the current status or rather with a status of `[Pending]` or `[Completed]`.
- Shows a message if no tasks are found .
### `complete_task(task_numbers)`

**Purpose:**  
Complete one or more tasks.

**Functionality:**  
- Accept a single parameter **task_numbers** a string. This parameter will be comma separated string of task numbers where each task number is a number between 1 and total number of tasks.
- Parse the comma, delimited to get individual task numbers.
- Validate whether each task number is valid or not.
- Make sure that the given task number is valid the task, then update `status` `[Completed]` and it was `[Pending]`.
- Shows message for completed tasks for users to view and make sure it updates for not appearing completed.
- Update the `tasks.txt` file to what all changes made to the list of tasks.

### `delete_task(task_numbers)`

**Purpose:**  
Delete one or more tasks from the list.

**Functionality:**  
- It receives a string of comma separated numbers `task_numbers`.
- Parse it to a correct task number, individual one.
- For each task number, it checks if it out of bound (the range of current tasks).
- It removes the tasks that are listed in the reverse order of numbers in order that there may not be any index out of bound error.
- Outputs displays for deleted task and invalid input in the task number.
 - Updates the `tasks.txt` file with the newly updated list of tasks.

### `main()`

**Purpose:**  
Interprets user input and based on that, it makes the calls to the functions as demanded by the passed arguments.

**Functionality:**  
- It repeatedly displays a menu showing what actions the user can take.
- It prompts the user to choose an option to add a task, view tasks, complete a task, delete a task, or to quit.
- Invokes the function as per told by the user's decision.
- It saves the application when it determines that the user decides to do so.

## Usage

1. **Add Tasks:**  
   This option can add many tasks with descriptions where the descriptions should have a comma in between.

2. **View Tasks:**  
   Here, one can view all tasks plus statuses that the tasks have been at the moment.

3. **Complete Tasks:**
Use the following option to checkmark the tasks from the list by just providing their numbers separated by commas.

4. **Delete Tasks:**  
  Use to delete tasks by entering the task number from the list, separated by commas.

5. **Exit:**  
  Use to exit the application.
