import json
import os
import datetime
import Tasks

def get_int():
    while True:
        try:
            result = int(input())
        except ValueError as val:
            print("Please enter only integers")
            continue
        return result
    
def get_saves_as_dct():
    Tasks.check_saves_exist()
    with open("saves.json", "r") as file:
        saves = json.load(file)
    
    return saves

if __name__ == "__main__":
    Tasks.check_saves_exist()

    while True:
        print("\n Chose what to do:\n1. List all tasks\n2. List all finished tasks\n3. List all unfinished tasks\n4. List all tasks that are in progress\n5. Add a new task\n6. Update existing task\n7. Delete taks")
        try:
            action = int(input())
        except ValueError as val:
            print("Please write only integers from 1 to 7.")
            continue
        
        saves = get_saves_as_dct()
        if action == 1: # prints all tasks
            if len(saves["saved_tasks"]) == 0:
                print("No saved tasks found")
            
            else:
                for task in saves["saved_tasks"]:
                    Tasks.print_task(task)
        
        elif action == 2: # prints only tasks that are done
            if len(saves["saved_tasks"]) == 0:
                print("No saved tasks found")
            
            else:
                flag = True
                for task in saves["saved_tasks"]:
                    if task["status"] == "Done":
                        Tasks.print_task(task)
                        flag = False
                if flag == True:
                    print("No finished tasks found")
        
        elif action == 3:
            if len(saves["saved_tasks"]) == 0:
                print("No saved tasks found")
            
            else:
                for task in saves["saved_tasks"]:
                    if task["status"] != "Done":
                        Tasks.print_task(task)
        
        elif action == 4:
            if len(saves["saved_tasks"]) == 0:
                print("No saved tasks found")
            
            else:
                for task in saves["saved_tasks"]:
                    if task["status"] == "Done":
                        Tasks.print_task(task)

        elif action == 5:
            del saves
            Tasks.create_new_task()

        elif action == 6:
            print("Chose a task you want to update: ")
            ids_and_names = {}
            for task in saves["saved_tasks"]:
                task_id = task.get("id")
                task_name = task.get("name")
                ids_and_names[task_id] = task_name
            
            for key in ids_and_names:
                print(f"{key}: {ids_and_names.get(key)}")

            while True:
                action = get_int()
                if action in ids_and_names:
                    break
            
            