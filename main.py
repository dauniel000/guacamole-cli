import os
from PIL import Image, ImageDraw, ImageFont
import settings
from support.setter import set_wallpaper
from utils.todos import load_todos, save_todos
from utils.render_wallpaper import render_wallpaper
import sys


def print_help():
    print("""
ToDo CLI Usage:
  python main.py list         # List all todos
  python main.py add          # Add a new todo (prompts for input)
  python main.py rm <index>   # Remove todo by index (1-based)
  python main.py remove <index> # Same as rm
  python main.py flush        # Remove all todos
  python main.py help         # Show this help message
""")


def main():
    args = sys.argv[1:]
    if not args or args[0] == 'help':
        print_help()
        return
    cmd = args[0]
    if cmd == 'list':
        todos = load_todos()
        print("\nAll tasks:")
        for i, todo in enumerate(todos, 1):
            print(f"{i}. {todo}")
    elif cmd == 'add':
        todos = load_todos()
        if len(args) > 1:
            action = ' '.join(args[1:]).strip()
        else:
            action = input("Create a new task: ").strip()
        if action:
            todos.append(action)
            save_todos(todos)
            print("Created task!")
        render_wallpaper(todos)
        set_wallpaper(settings.WALLPAPER_FILE)
    elif cmd in ('rm', 'remove'):
        todos = load_todos()
        if len(args) < 2 or not args[1].isdigit():
            print("Give a index of task, np. python main.py rm 2")
            return
        idx = int(args[1]) - 1
        if 0 <= idx < len(todos):
            removed = todos.pop(idx)
            save_todos(todos)
            print(f"Removed: {removed}")
            render_wallpaper(todos)
            set_wallpaper(settings.WALLPAPER_FILE)
        else:
            print("Invalid task number.")
    elif cmd == 'flush':
        save_todos([])
        render_wallpaper([])
        set_wallpaper(settings.WALLPAPER_FILE)
        print("All tasks cleared!")
    else:
        print_help()

if __name__ == "__main__":
    main()