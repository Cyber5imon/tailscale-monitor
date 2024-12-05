## Tailscale Device Monitor

This Python script monitors the status of devices on your Tailscale network and sends desktop notifications when devices go online or offline.

## Installation

1. **Install Required Packages:**

```bash
pip install tailscale notify2
```

2. **Obtain Your Tailscale API Key:**

   1. Log in to your Tailscale account.
   2. Navigate to the **Admin** section of your Tailnet.
   3. Go to the **Keys** page.
   4. Generate a new API access token.
   5. Copy the generated token.

## Usage

1. **Replace Placeholders:**

   - Open the `tailscale_monitor.py` script.
   - Replace `your_tailnet_name` with your actual Tailnet name.
   - Replace `your_api_key` with the API key you generated.

2. **Run the Script:**

```bash
python tailscale_monitor.py
```

## How it Works

1. **Fetches Device List:** The script retrieves a list of all devices in your Tailnet using the Tailscale API.
2. **Monitors Device Status:** It continuously checks the status of each device.
3. **Sends Notifications:** When a device's status changes (online or offline), a desktop notification is displayed.

## Customization

* **Polling Interval:** Adjust the `asyncio.sleep(60)` interval to change how often the script checks device status.
* **Notification Customization:** You can further customize notifications by modifying the `notify2.Notification` parameters.
* **Error Handling:** Implement error handling to gracefully handle exceptions and log errors.
* **Device Filtering:** You can modify the script to monitor only specific devices by filtering the device list.

## Note

* **API Rate Limits:** Be mindful of Tailscale's API rate limits. For large-scale monitoring, consider implementing more efficient polling strategies or using webhooks.
* **API Key Security:** Treat your API key as sensitive information. Do not share it publicly.
* **Notification Preferences:** Configure your desktop notification settings to ensure you receive alerts.

By following these steps and customizing the script to your needs, you can effectively monitor your Tailscale network and stay informed about device status changes.
