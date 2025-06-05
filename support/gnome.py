import subprocess
import os

def set_gnome_wallpaper(filepath):
    abs_path = os.path.abspath(filepath)
    uri = f"file://{abs_path}"
    if subprocess.call(["which", "gsettings"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
        print("gsettings command not found. Cannot set wallpaper.")
        return
    try:
        result1 = subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", uri], capture_output=True, text=True)
        result2 = subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri-dark", uri], capture_output=True, text=True)
        if result1.returncode != 0:
            print(f"Error setting picture-uri: {result1.stderr}")
        if result2.returncode != 0:
            print(f"Error setting picture-uri-dark: {result2.stderr}")
    except Exception as e:
        print(f"Nie udało się ustawić tapety: {e}")
