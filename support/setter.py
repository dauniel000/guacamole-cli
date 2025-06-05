import platform
import os
from support.kde import set_kde_wallpaper
from support.gnome import set_gnome_wallpaper
from support.windows import set_windows_wallpaper

def set_wallpaper(filepath):
    system = platform.system()
    if system == "Linux":

        desktop_env = os.environ.get("XDG_CURRENT_DESKTOP", "").lower()
        
        if "gnome" in desktop_env:
            set_gnome_wallpaper(filepath)
        elif "kde" in desktop_env or "plasma" in desktop_env:
            set_kde_wallpaper(filepath)
        else:
            print(f"Nieobsługiwane środowisko graficzne: {desktop_env}")
    elif system == "Windows":
        set_windows_wallpaper(filepath)
    else:
        print("Zmiana tapety nie jest wspierana na tym systemie")
