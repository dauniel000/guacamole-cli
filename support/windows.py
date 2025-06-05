import os
import ctypes

def set_windows_wallpaper(filepath):
    abs_path = os.path.abspath(filepath)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 3)
