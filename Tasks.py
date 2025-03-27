import json

def get_id():
    with open("saves.json", "r") as file:
        saves = json.load(file)
        list_of_ids = []
        for task in saves["saved_tasks"]:
            list_of_ids.append(task.get("id"))
        return list_of_ids

print(get_id())

def create_new_task(id):
    id = 3