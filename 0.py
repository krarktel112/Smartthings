import requests

#base_url = "https://api.voicemonkey.io/trigger"
#access_token = "<your_access_token>"
#secret_token = "<your_secret_token>"
#monkey = "<your_monkey_id>"
#announcement = "<your_announcement_text>" # Optional: for announcement

#payload = {
#    "access_token": access_token,
#    "secret_token": secret_token,
#    "monkey": monkey,
#    "announcement": announcement  # Include if you want to make an announcement
#}

#try:
    #response = requests.get(base_url, params=payload)
requests.get(https://api-v2.voicemonkey.io/trigger?token=b2ca9b305243e72ddc48196c3059e232_ed99b6d5eeeeb967306f6d3d703ecda2&device=echo1)
    #response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    #print("Voice Monkey triggered successfully.")
#except requests.exceptions.RequestException as e:
    #print(f"Error triggering Voice Monkey: {e}")
