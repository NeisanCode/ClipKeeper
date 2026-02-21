from datetime import datetime
import pyperclip
import threading
import time
from repo import savejson


def monitor_clipboard(reload: callable):
    print("Starting clipboard monitor...")
    last = pyperclip.paste()
    while True:
        current = pyperclip.paste()
        if current != last:
            savejson.save_clip(current)
            last = current
            reload()
            print(f"New clip saved: {current}")
        time.sleep(1)


def watcher_clipper(reload: callable):
    threading.Thread(target=monitor_clipboard, args=(reload,), daemon=True).start()