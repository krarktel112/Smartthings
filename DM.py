import time
import json
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def read_config_json(file_path):
    try:
        with open(file_path, 'r') as file:
            config_data= json.load(file)
            return config_data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' contains invalid JSON.")
    except  Exception as e:
        print(f"An unexpected error occured: {e}")
        return None

config_file_path = r"C:\Users\User\AppData\Roaming\BetterDiscord\plugins\MessageLoggerV2Data.config.json"
config_file_path2 = r"C:\Users\User\AppData\Roaming\BetterDiscord\plugins\MessageLoggerV2Data.config.json"
config = read_config_json(config_file_path)
y = "pop"

class FileOpenHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
            config = read_config_json(config_file_path)
            x = event.src_path
            user = "Korra"
            #print(f"File opened: {event.src_path} {timestamp_str} {config}")
            if x == config_file_path2:
                python3 Messages.py 260341 verizon dm

def watch_directory(path):
    observer = Observer()
    event_handler = FileOpenHandler()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    path_to_watch = r"C:\Users\User\AppData\Roaming\BetterDiscord\plugins"  # Replace with the directory you want to watch
    watch_directory(path_to_watch)
