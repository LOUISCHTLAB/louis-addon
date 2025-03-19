import asyncio
import os
import aioesphomeapi
from aioesphomeapi import APIClient, APIConnectionError

async def connect_and_log():
    device_ip = os.environ.get('DEVICE_IP')
    port = os.environ.get('PORT', '6053')  # Default port if not set
    password = os.environ.get('PASSWORD')
    encryption_key = os.environ.get('ENCRYPTION_KEY')

    try:
        print(f"Attempting to connect to {device_ip}:{port} with password: {password is not None}, encryption_key: {encryption_key is not None}")
        client = APIClient(
            host=device_ip,
            port=int(port),
            password=password if password else None,
            encryption_key=encryption_key if encryption_key else None
        )
        await client.connect(login=True)
        print(f"Connected to ESPHome device at {device_ip}:{port} successfully!")

        async for log in client.subscribe_logs():
            print(f"ESPHome Log: {log.message}")
            # bashio::log.info(f"ESPHome Log: {log.message}")

    except APIConnectionError as e:
        print(f"Connection Error: {e}")
        # bashio::log.error(f"Connection Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
        # bashio::log.error(f"Unexpected Error: {e}")
    finally:
        if 'client' in locals():
            await client.disconnect()
            print("Disconnected from ESPHome device.")
            # bashio::log.info("Disconnected from ESPHome device.")

# Run the async function
asyncio.run(connect_and_log())