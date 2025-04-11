import requests

url = "https://api-v2.voicemonkey.io/trigger?token=b2ca9b305243e72ddc48196c3059e232_ed99b6d5eeeeb967306f6d3d703ecda2&device=echo1"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    
    # Access the content of the response
    html_content = response.text
    print(html_content)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
