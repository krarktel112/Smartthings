import requests 

dnd = 'https://api-v2.voicemonkey.io/trigger?token=b2ca9b305243e72ddc48196c3059e232_ed99b6d5eeeeb967306f6d3d703ecda2&device=ashley-dnd'
off = 'https://api-v2.voicemonkey.io/trigger?token=b2ca9b305243e72ddc48196c3059e232_ed99b6d5eeeeb967306f6d3d703ecda2&device=ashley-off'
on = 'https://api-v2.voicemonkey.io/trigger?token=b2ca9b305243e72ddc48196c3059e232_ed99b6d5eeeeb967306f6d3d703ecda2&device=ashley-on'
idle = 'https://api-v2.voicemonkey.io/trigger?token=b2ca9b305243e72ddc48196c3059e232_ed99b6d5eeeeb967306f6d3d703ecda2&device=ashley-idle'
listening = 'https://api-v2.voicemonkey.io/trigger?token=b2ca9b305243e72ddc48196c3059e232_ed99b6d5eeeeb967306f6d3d703ecda2&device=ashley-listening'
game = 'https://api-v2.voicemonkey.io/trigger?token=b2ca9b305243e72ddc48196c3059e232_ed99b6d5eeeeb967306f6d3d703ecda2&device=ashley-game'
play = 'https://api-v2.voicemonkey.io/trigger?token=b2ca9b305243e72ddc48196c3059e232_ed99b6d5eeeeb967306f6d3d703ecda2&device=ashley-playing'

y =input("intra")
def plura(intra):
  if intra == "online":
    response = requests.get('https://api-v2.voicemonkey.io/trigger?token=b2ca9b305243e72ddc48196c3059e232_ed99b6d5eeeeb967306f6d3d703ecda2&device=ashley-on')
    response.raise_for_status()
  elif intra = "offline":
    response = requests.get('https://api-v2.voicemonkey.io/trigger?token=b2ca9b305243e72ddc48196c3059e232_ed99b6d5eeeeb967306f6d3d703ecda2&device=ashley-off')
    response.raise_for_status()
  else:
    response = requests.get('https://api-v2.voicemonkey.io/trigger?token=b2ca9b305243e72ddc48196c3059e232_ed99b6d5eeeeb967306f6d3d703ecda2&device=ashley-idle)
    response.raise_for_status()
