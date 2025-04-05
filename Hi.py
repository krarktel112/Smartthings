import SmartThings

token = '372563b7-09f8-485b-8c95-261793424ad9'
ST = SmartThings.Account(token)
print("scenes")
print(ST.scenes)
print("devices")
print(ST.devices)
print("locations")
print(ST.locations)
