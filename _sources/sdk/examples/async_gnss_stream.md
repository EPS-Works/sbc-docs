<!-- markdownlint-disable-next-line MD041 -->
### Asynchronous GNSS Message Handler

This script sets up an asynchronous handler to process NMEA GGA messages from a GNSS module. It initializes a serial buffer cursor for the GNSS1 device, launches a background task to parse data from the incoming stream, and leaves the main loop open for additional tasks or logic.

```python
from sbc import GNSS1
from sdk import Stream, SerialBuffer
from sdk.parsers import NMEA
from asyncio import sleep, create_task, run

async def handle_gga(cursor):
    with Stream(cursor, parsers=[NMEA]) as stream:
        async for msg in stream:
            print(msg.lat, msg.lon, msg.fix)

async def main():
    GNSS1.stream(messages=['GGA'], port=1)
    
    buffer = SerialBuffer(GNSS1)
    create_task(handle_gga(buffer.cursor('__gga__')))

    while True:
        # Your magic here... 🎉
        
        await sleep(5)

if __name__ == '__main__':
    run(main())
```

```{eval-rst}
.. nextprev::
```
