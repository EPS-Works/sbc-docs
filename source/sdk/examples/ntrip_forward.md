<!-- markdownlint-disable-next-line MD041 -->
### Asynchronous RTK Correction Bridge Using NTRIP and GNSS

This script sets up an RTK correction bridge using NTRIP caster to enhance GNSS positioning. It connects to a network, creates a serial buffer cursor for GNSS1 to stream GGA messages, and launches an asynchronous task that feeds RTK correction data into the GNSS pipeline. The main loop remains available for user-defined tasks.

```python
from sbc import GNSS1, Ethernet
from sdk import SerialBuffer
from ntrip import NTRIPClient, RTKBridge
from asyncio import run, create_task, sleep

# Extract to config file
NETWORK_CONFIG = {
  'ip': '192.168.1.20',
  'gateway': '192.168.1.1',
}

NTRIP_CONFIG = {
    'host': '192.148.213.42',
    'port': 2101,
    'mountpoint': '__mountpoint__',
    'user': '*********',
    'password': '*********',
}


async def main():
    """Main application"""
    Ethernet.connect(**NETWORK_CONFIG)
    print(f'Connected as {Ethernet.ip}')
    
    # Start streaming GGA from GNSS1
    GNSS1.stream(messages=['GGA'], port=1)
    
    # Create a buffer cursor for concurrent GNSS1 reads
    buffer = SerialBuffer(GNSS1)
    cursor = buffer.cursor('__ntrip__')
    
    # Run the bridge asynchronously
    client = NTRIPClient(**NTRIP_CONFIG)
    bridge = RTKBridge(client)
    rtk = create_task(bridge.run(cursor))
    
    try: 
        while True:
            # Your magic here... 🎉
            await sleep(1)
    finally:
        rtk.cancel()


if __name__ == "__main__":
    run(main())
```

```{eval-rst}
.. nextprev::
```
