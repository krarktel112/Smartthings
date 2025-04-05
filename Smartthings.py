import aiohttp
import pysmartthings

async def control_switch(device_id, action):
    token = "YOUR_SMARTTHINGS_TOKEN"  # Replace with your actual token
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
device_id_to_control = "YOUR_DEVICE_ID"  # Replace with the actual device ID
await control_switch(device_id_to_control, "on")
await control_switch(device_id_to_control, "off")
