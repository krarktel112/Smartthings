import asyncio
from pysmartthings import SmartThings

async def main():
    # Replace with your SmartThings personal access token
    token = "372563b7-09f8-485b-8c95-261793424ad9"

    # Create a SmartThings client
    async with SmartThings(token) as smartthings:
        # Get all devices
        devices = await smartthings.devices()

        # Print the name of each device
        for device in devices:
            print(device.label)

        # Control a specific device (e.g., turn on a light)
        light = next(dev for dev in devices if dev.label == "My Light")
        if light:
            await light.switch_on()

if __name__ == "__main__":
    asyncio.run(main())
