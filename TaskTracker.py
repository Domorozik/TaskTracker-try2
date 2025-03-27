import json
import os
import datetime




if __name__ == "__main__":
    check_saves_exist()

    while True:
        print("\n Chose what to do:\n1. List all tasks\n2. List all finished tasks\n3. List all unfinished tasks\n4. List all tasks that are in progress\n5. Add a new task\n6. Update existing task\n7. Delete taks")
        try:
            action = int(input())
        except ValueError as val:
            print("Please write only integers from 1 to 7.")
        
