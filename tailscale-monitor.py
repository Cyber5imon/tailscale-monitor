import asyncio
import time
from tailscale import Tailscale
import notify2

async def monitor_all_devices(tailnet, api_key):
    notify2.init("Tailscale Device Monitor")

    async with Tailscale(tailnet=tailnet, api_key=api_key) as tailscale:
        while True:
            devices = await tailscale.devices()

            for device in devices:
                device_address = device['address']
                device_name = device['name']
                device_status = device['status']

                if device_status == 'up':
                    notification = notify2.Notification(
                        "Tailscale Device Online", f"{device_name} ({device_address}) is online"
                    )
                    notification.show()
                else:
                    notification = notify2.Notification(
                        "Tailscale Device Offline", f"{device_name} ({device_address}) is offline"
                    )
                    notification.show()

            await asyncio.sleep(60)  # Adjust the polling interval as needed


# Replace with your actual Tailnet and API key
tailnet = "your_tailnet_name"
api_key = "your_api_key"

asyncio.run(monitor_all_devices(tailnet, api_key))