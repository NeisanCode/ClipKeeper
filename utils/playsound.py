import subprocess
import sys



def playsound(path: str):
    if sys.platform == "win32":
        import winsound
        winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC)
    elif sys.platform == "darwin":
        subprocess.Popen(["afplay", path])
    else:  # Linux
        subprocess.Popen(
            ["paplay", path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
