import aiohttp
import pysmartthings

token = '372563b7-09f8-485b-8c95-261793424ad9'

async with aiohttp.ClientSession() as session:
    api = pysmartthings.SmartThings(session, token)
    locations = await api.locations()
    print(len(locations))

    location = locations[0]
    print(location.name)
    print(location.location_id)
