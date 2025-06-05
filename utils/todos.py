import os
import settings

def load_todos():
    if not os.path.exists(settings.TODO_FILE):
        return []
    
    with open(settings.TODO_FILE, 'r') as file:
        return [line.strip() for line in file.readlines()]

def save_todos(todos):
    with open(settings.TODO_FILE, "w") as file:
        file.write("\n".join(todos))
