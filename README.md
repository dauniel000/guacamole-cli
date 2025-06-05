# Guacamole CLI

Guacamole CLI is a cross-platform tool that turns your to-do list into a beautiful desktop wallpaper. It supports KDE Plasma, GNOME, and Windows environments, and is written in Python.

> **Disclaimer:** Guacamole CLI has only been thoroughly tested on KDE Plasma. Support for GNOME and Windows is experimental.

## Features
- Manage your to-do list from the command line
- Automatically updates your desktop wallpaper with your tasks
- Customizable background image and appearance
- Supports KDE Plasma, GNOME, and Windows

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/guacamole-cli.git
   cd guacamole-cli
   ```
2. **Install dependencies:**
   ```sh
   pip install pillow
   ```
   - For KDE Plasma: `sudo pacman -S qt5-tools` and ensure `qdbus` is installed
   - For GNOME: Make sure `gsettings` is available

## Usage

Run the CLI with Python:

```sh
python main.py [command] [arguments]
```

### Commands
- `list` — List all todos
- `add [task]` — Add a new todo (if no task is given, prompts for input)
- `rm <index>` or `remove <index>` — Remove a todo by its index (1-based)
- `flush` — Remove all todos
- `help` — Show help message

### Example
```sh
python main.py add "Buy groceries"
python main.py list
python main.py rm 1
python main.py flush
```

## Customization
- Change the background image by replacing `background.jpg` or editing `USER_WALLPAPER` in `settings.py`.
- Adjust colors, font size, and dimensions in `settings.py`.

## Demo Video

You can watch a demo of the tool in action below:

[▶️ Watch demo video](video/demo.mp4)

## Contributing
- Create a fork
- Make a feature
- Push it to GitHub
- Create a pull request!

## License
This project is licensed under the GNU GPL v3. See the LICENSE file for details.




