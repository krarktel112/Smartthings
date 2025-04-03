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
if config:
    print(config)
    if (config = ("{'settings': {'setting1': 'online'}}")):
        print("Online")
    elif(config = ("{'settings': {'setting1': 'idle'}}")):
        print("Idle")
    elif(config = ("{'settings': {'setting1': 'dnd'}}")):
        print("DND")
    elif(config = ("{'settings': {'setting1': 'gaming'}}")):
        print("Gaming")
    elif(config = ("{'settings': {'setting1': 'playing'}}")):
        print("Playing")
    elif(config = ("{'settings': {'setting1': 'listening'}}")):
        print("Listening")
    elif(config = ("{'settings': {'setting1': 'streaming'}}")):
        print("Streaming")
    else:
        print(config)
else:
    print("Failed to load configuration.")
