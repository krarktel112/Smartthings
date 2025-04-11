import requests

base_url = "https://api.voicemonkey.io/trigger"
access_token = "b2ca9b305243e72ddc48196c3059e232_ed99b6d5eeeeb967306f6d3d703ecda2"
secret_token = "b2ca9b305243e72ddc48196c3059e232_ed99b6d5eeeeb967306f6d3d703ecda2&device=echo1"
#monkey = "<your_monkey_id>"
#announcement = "<your_announcement_text>" # Optional: for announcement

payload = {
    "access_token": access_token,
    "secret_token": secret_token,
#    "monkey": monkey,
#    "announcement": announcement  # Include if you want to make an announcement
}

try:
    response = requests.get(base_url, params=payload)
    print("Voice Monkey triggered successfully.")
except requests.exceptions.RequestException as e:
    print(f"Error triggering Voice Monkey: {e}")
