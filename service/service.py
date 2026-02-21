from datetime import datetime
import pyperclip
import threading
import time
from repo import savejson

def monitor_clipboard():
    last = pyperclip.paste()
    while True:
        current = pyperclip.paste()
        if current != last:
            savejson.save_clip(current, datetime.now().isoformat())
            last = current
        time.sleep(1)


def watcher_clipper():
    threading.Thread(target=monitor_clipboard, daemon=True).start()