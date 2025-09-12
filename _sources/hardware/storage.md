# Storage

The SBC features a dual-storage system designed for flexibility and ease of access:

- 16 MB onboard external flash memory
- microSD card slot, supporting cards up to 32 GB

At runtime, the SBC automatically selects its primary storage based on the presence of a microSD card: If a microSD card is inserted, it takes priority and is used as the main memory. If no card is present, the SBC falls back to the external flash.

This design ensures seamless operation whether or not removable storage is used.

When the SBC is connected to a host computer via USB, the currently active main memory, whether flash or microSD, is exposed as a mass storage device, making file management as simple as drag and drop.

This setup enables fast prototyping, remote updates, and straightforward file transfer without needing custom tools or drivers.

For examples about how to use the external flash or microSD memory, you can also refer to the [Storage Reference](../sdk/reference/storage).
