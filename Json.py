import json

with open("data.json", "r") as file:
    line = file.readline(-3)
    try:
        data = json.loads(line)
        print(data["name"])
        print(data["age"])
        print(data["city"])
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
