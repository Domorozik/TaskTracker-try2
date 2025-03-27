import json
from pathlib import Path

def check_saves_exist(file_name = 'saves.json', default_data: dict = None) -> bool:
    if default_data is None:
        default_data = {"saved_tasks" : []}

        file_path = Path(file_name)

        if not file_path.exists():
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(default_data, file, indent=4, ensure_ascii=False)
                print(f"Файл для сохранения задач {file_name} создан в {file_name}")
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

def create_new_task():
    id = get_id()
    print(id)

create_new_task()