import json
import datetime
from pathlib import Path

def get_time():
    return str(datetime.datetime.now())[:-7]

def enter_name():
    return input("\nEnter name for the task: ")

def enter_description():
    return input("Enter description for a new task: ")

def enter_task_status(name: str, previous_status: str = "In progress",):
    while True:
        print(f"\nEnter status for task {name}:\n1. In progres\n2. Done\n3. Postponded\n4. Go back")
        try:
            status = int(input())
        except ValueError as val:
            print("Please enter an integer from 1 to 4")
        if status == 1:
            return "In progres"
        elif status == 2:
            return "Done"
        elif status == 3:
            return "Postponded"
        elif status == 4:
            return previous_status
        else:
            pass
        
def check_saves_exist():
    file_name = 'saves.json'
    default_data = {"saved_tasks" : []}

    file_path = Path(file_name)

    if not file_path.exists():
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(default_data, file, indent=4, ensure_ascii=False)
            print(f"Файл для сохранения задач {file_name} создан в {file_path}")
            file.close()
            return True
        except Exception as exc:
            print(f"Ошибка при создании файла:\n{exc}")
            raise
    else:
        return False

def get_id():
    check_saves_exist()
    with open("saves.json", "r") as file:
        saves = json.load(file)
        list_of_ids = []

    set_of_ids = {task.get("id") for task in saves["saved_tasks"]}

    new_id = 0

    while new_id in set_of_ids:
        new_id += 1
    
    return new_id

def print_task(task:dict):
    print(f"\n\n*** Printing task {task.get("name")} ***\n")

    for key in task:
        print(f"{key} : {task.get(key)}")

def create_new_task():
    task_id = get_id()
    print(f"\n\n*** Creating new task with id: {task_id} ***")
    name = enter_name()
    description = enter_description()
    created_at = get_time()
    status = "In progress"
    
    new_task = {
        "id" : task_id,
        "name" : name,
        "description" : description,
        "created at" : created_at,
        "status" : status
    }

    with open("saves.json", "r") as file:
        saves = json.load(file)
        saves["saved_tasks"].append(new_task)
    
    with open("saves.json", "w") as file:
        json.dump(saves, file, indent=4, ensure_ascii=False)

create_new_task()    