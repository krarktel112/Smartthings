import aiohttp
import pysmartthings

async def control_switch(device_id, action):
    token = "372563b7-09f8-485b-8c95-261793424ad9"  # Replace with your actual token
    async with aiohttp.ClientSession() as session:
        api = pysmartthings.SmartThings(session, token)
        device = await api.devices.get(device_id)
        
        if action == "on":
            await device.command("main", "switch", "on")
            print(f"Turned on device: {device.label}")
        elif action == "off":
            await device.command("main", "switch", "off")
            print(f"Turned off device: {device.label}")
        else:
            print("Invalid action. Use 'on' or 'off'.")

# Example usage:
device_id_to_control = "96ce780f-8c5d-4f3b-adc9-a368875a3343"  # Replace with the actual device ID
control_switch(device_id_to_control, "on")
control_switch(device_id_to_control, "off")
