from datetime import datetime
import pyperclip
import threading
import time
from utils import savejson

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

print("Starting clipboard watcher...")
watcher_clipper()
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
        break
