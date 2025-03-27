import json
import os
import datetime
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
            print(f"Файл {file_name} уже сущетсвует")
            return False

if __name__ == "__main__":
    check_saves_exist()

    while True:
        print("\n Chose what to do:\n1. List all tasks\n2. List all finished tasks\n3. List all unfinished tasks\n4. List all tasks that are in progress\n5. Add a new task\n6. Update existing task\n7. Delete taks")
        try:
            action = int(input())
        except ValueError as val:
            print("Please write only integers from 1 to 7.")
        
