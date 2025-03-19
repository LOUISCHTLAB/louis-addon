import asyncio
import aioesphomeapi
from aioesphomeapi import APIClient, APIConnectionError

async def connect_and_log(device_ip, port, password, encryption_key):
    try:
        # Create API client
        client = APIClient(
            host=device_ip,
            port=int(port),
            password=password if password else None,
            encryption_key=encryption_key if encryption_key else None
        )
        await client.connect(login=True)
        bashio::log.info(f"Connected to ESPHome device at {device_ip}:{port} successfully!")

        # Subscribe to logs
        async for log in client.subscribe_logs():
            bashio::log.info(f"ESPHome Log: {log.message}")

    except APIConnectionError as e:
        bashio::log.error(f"Failed to connect: {e}")
    except Exception as e:
        bashio::log.error(f"An error occurred: {e}")
    finally:
        await client.disconnect()

# Get environment variables from bashio (passed via run.sh)
device_ip = "${device_ip}"
port = "${port}"
password = "${password}"
encryption_key = "${encryption_key}"

# Run the async function
asyncio.run(connect_and_log(device_ip, port, password, encryption_key))