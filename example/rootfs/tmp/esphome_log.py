import asyncio
import aioesphomeapi
from aioesphomeapi import APIClient, APIConnectionError

async def connect_and_log(device_ip, port, password, encryption_key):
    try:
        # Log thông tin kết nối
        print(f"Attempting to connect to {device_ip}:{port} with password: {password is not None}, encryption_key: {encryption_key is not None}")
        # Create API client
        client = APIClient(
            host=device_ip,
            port=int(port),
            password=password if password else None,
            encryption_key=encryption_key if encryption_key else None
        )
        await client.connect(login=True)
        print(f"Connected to ESPHome device at {device_ip}:{port} successfully!")

        # Subscribe to logs
        async for log in client.subscribe_logs():
            print(f"ESPHome Log: {log.message}")  # In ra console trước
            bashio::log.info(f"ESPHome Log: {log.message}")  # Gửi log qua bashio

    except APIConnectionError as e:
        print(f"Connection Error: {e}")
        bashio::log.error(f"Connection Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
        bashio::log.error(f"Unexpected Error: {e}")
    finally:
        if 'client' in locals():
            await client.disconnect()
            print("Disconnected from ESPHome device.")
            bashio::log.info("Disconnected from ESPHome device.")

# Get environment variables from bashio (passed via run.sh)
device_ip = "${device_ip}"
port = "${port}"
password = "${password}"
encryption_key = "${encryption_key}"

# Run the async function
asyncio.run(connect_and_log(device_ip, port, password, encryption_key))