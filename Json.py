import json

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
config_file_path = r"C:\Users\User\AppData\Roaming\BetterDiscord\plugins\Aoffline.config.json"
config = read_config_json(config_file_path)
online = "online"
idle = "idle"
dnd = "dnd"
gaming = "gaming"
streaming = "streaming"
listening = "listening"
playing = "playing"
if config:
    print(config)
    if online in config:
        print("Online")
    elif idle in config:
        print("Idle")
    elif dnd in config:
        print("DND")
    elif gaming in config:
        print("Gaming")
    elif playing in config:
        print("Playing")
    elif listening in config:
        print("Listening")
    elif streaming in config:
        print("Streaming")
    else:
        print(config)
else:
    print("Failed to load configuration.")
