import os
import subprocess

def set_kde_wallpaper(filepath):
    abs_path = os.path.abspath(filepath)

    if subprocess.call(["which", "plasma-apply-wallpaperimage"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
        try:
            result = subprocess.run(["plasma-apply-wallpaperimage", abs_path], capture_output=True, text=True)
            if result.returncode != 0:
                print(f"Error setting KDE wallpaper with plasma-apply-wallpaperimage: {result.stderr}")
            else:
                print("Wallpaper set using plasma-apply-wallpaperimage.")
            return
        except Exception as e:
            print(f"Nie udało się ustawić tapety przez plasma-apply-wallpaperimage: {e}")

    qdbus_cmd = None
    for cmd in ["qdbus", "qdbus-qt5"]:
        if subprocess.call(["which", cmd], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
            qdbus_cmd = cmd
            break
    if not qdbus_cmd:
        print("Neither plasma-apply-wallpaperimage, qdbus nor qdbus-qt5 found. Cannot set wallpaper on KDE/Plasma.")
        return
    uri = f"file://{abs_path}"
    uri3 = f"file:///{abs_path.lstrip('/')}"
    script = (
        "var allDesktops = desktops(); "
        "for (i=0;i<allDesktops.length;i++) { "
        "d = allDesktops[i]; "
        "d.wallpaperPlugin = 'org.kde.image'; "
        "d.currentConfigGroup = Array('Wallpaper', 'org.kde.image', 'General'); "
        f"d.writeConfig('Image', '{uri}'); "
        "}"
    )
    try:
        result = subprocess.run([
            qdbus_cmd, "org.kde.plasmashell", "/PlasmaShell", "org.kde.PlasmaShell.evaluateScript", script
        ], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error setting KDE wallpaper with file://: {result.stderr}\nTrying with file:/// ...")

            script3 = (
                "var allDesktops = desktops(); "
                "for (i=0;i<allDesktops.length;i++) { "
                "d = allDesktops[i]; "
                "d.wallpaperPlugin = 'org.kde.image'; "
                "d.currentConfigGroup = Array('Wallpaper', 'org.kde.image', 'General'); "
                f"d.writeConfig('Image', '{uri3}'); "
                "}"
            )
            result3 = subprocess.run([
                qdbus_cmd, "org.kde.plasmashell", "/PlasmaShell", "org.kde.PlasmaShell.evaluateScript", script3
            ], capture_output=True, text=True)
            if result3.returncode != 0:
                print(f"Error setting KDE wallpaper with file:///: {result3.stderr}")
            else:
                print("Wallpaper set using file:/// prefix.")
        else:
            print("Wallpaper set using file:// prefix.")
    except Exception as e:
        print(f"Cannot set Wallpaper on KDE: {e}")
