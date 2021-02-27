# https://tutorialedge.net/python/concurrency/asyncio-event-loops-tutorial/
import os, sys
import asyncio
import platform

from datetime import datetime
from typing import Callable, Any

from aioconsole import ainput
from bleak import BleakClient, discover

OurArduino33Ble = "MySensorForTests"


class Connection:
    client: BleakClient = None

    def __init__(
            self,
            loop: asyncio.AbstractEventLoop,
            accelX_characteristic: str,
            gyroX_characteristic: str,
            accelY_characteristic: str,
            gyroY_characteristic: str,
            accelZ_characteristic: str,
            gyroZ_characteristic: str,
            write_characteristic: str,
            data_dump_handler: Callable[[str], None],
            data_dump_size: int = 256,
    ):
        self.loop = loop
        self.accelX_characteristic = accelX_characteristic
        self.gyroX_characteristic = gyroX_characteristic
        self.accelY_characteristic = accelY_characteristic
        self.gyroY_characteristic = gyroY_characteristic
        self.accelZ_characteristic = accelZ_characteristic
        self.gyroZ_characteristic = gyroZ_characteristic
        self.write_characteristic = write_characteristic
        self.data_dump_handler = data_dump_handler

        self.last_packet_time = datetime.now()
        self.dump_size = data_dump_size
        self.connected = False
        self.connected_device = None
        self.rx_data = []
        self.rx_timestamps = []
        self.rx_delays = []

        self.n_probes_ax = 0
        self.n_probes_ay = 0
        self.n_probes_az = 0
        self.n_probes_gx = 0
        self.n_probes_gy = 0
        self.n_probes_gz = 0
        self.max_probes = 100

    def on_disconnect(self, client: BleakClient, future: asyncio.Future):
        self.connected = False
        # Put code here to handle what happens on disconnect.
        print(f"Disconnected from {self.connected_device.name}!")

    async def cleanup(self):
        if self.client:
            await self.client.stop_notify(self.gyroX_characteristic)
            await self.client.stop_notify(self.accelX_characteristic)
            await self.client.stop_notify(self.gyroY_characteristic)
            await self.client.stop_notify(self.accelY_characteristic)
            await self.client.stop_notify(self.gyroZ_characteristic)
            await self.client.stop_notify(self.accelZ_characteristic)
            await self.client.disconnect()

    async def manager(self):
        print("Starting connection manager.")
        while True:
            if self.client:
                await self.connect()
            else:
                await self.select_device()
                await asyncio.sleep(5.0)

    async def connect(self):
        if self.connected:
            return
        try:
            await self.client.connect()
            self.connected = await self.client.is_connected()
            if self.connected:
                print(F"Connected to {self.connected_device.name}")
                self.client.set_disconnected_callback(self.on_disconnect)
                await self.client.start_notify(
                    self.accelX_characteristic, self.accelX_notification_handler,
                )
                await self.client.start_notify(
                    self.gyroX_characteristic, self.gyroX_notification_handler,
                )
                await self.client.start_notify(
                    self.accelY_characteristic, self.accelY_notification_handler,
                )
                await self.client.start_notify(
                    self.gyroY_characteristic, self.gyroY_notification_handler,
                )
                await self.client.start_notify(
                    self.accelZ_characteristic, self.accelZ_notification_handler,
                )
                await self.client.start_notify(
                    self.gyroZ_characteristic, self.gyroZ_notification_handler,
                )
                while True:
                    if not self.connected:
                        break
                    await asyncio.sleep(1)
            else:
                print(f"Failed to connect to {self.connected_device.name}")
        except Exception as e:
            print(e)

    async def select_device(self):
        print("Bluetooh LE hardware warming up...")
        await asyncio.sleep(2.0)  # Wait for BLE to initialize.
        devices = await discover()
        devices = list(filter(lambda d: d.name != "Unknown", devices))
        deviceNames = list(map(lambda dev: dev.name, devices))
        if OurArduino33Ble in deviceNames:
            print(f"Found {OurArduino33Ble}")
            response = deviceNames.index(OurArduino33Ble)
        else:
            print("Please select device: ")
            for i, device in enumerate(devices):
                print(f"{i}: {device.name}")

            response = -1
            while True:
                response = await ainput("Select device: ")
                try:
                    response = int(response.strip())
                except:
                    print("Please make valid selection.")
                if response > -1 and response < len(devices):
                    break
                else:
                    print("Please make valid selection.")

        self.connected_device = devices[response]
        addressToConnect = devices[response].address
        print(f"Connecting..")
        self.client = BleakClient(addressToConnect)

    def record_time_info(self):
        present_time = datetime.now()
        self.rx_timestamps.append(present_time)
        self.rx_delays.append((present_time - self.last_packet_time).microseconds)
        self.last_packet_time = present_time

    def clear_lists(self):
        self.rx_data.clear()
        self.rx_delays.clear()
        self.rx_timestamps.clear()

    def accelX_notification_handler(self, sender: str, data: Any):
        #self.rx_data.append(int.from_bytes(data, byteorder="big"))
        if self.n_probes_ax > self.max_probes:
            return
        self.n_probes_ax += 1
        self.record_time_info()
        #if len(self.rx_data) >= self.dump_size:
        self.data_dump_handler("AX " + str(self.rx_timestamps[-1].time()) + " " + data.decode("utf-8"))
        # print(data.decode("utf-8") + "\n")
        with open("accelx_data.txt", "a") as f: # вставлено
            f.write(data.decode("utf-8") + "\n") # вставлено
        self.clear_lists()

    def gyroX_notification_handler(self, sender: str, data: Any):
        if self.n_probes_gx > self.max_probes:
            return
        self.n_probes_gx += 1
        #self.rx_data.append(int.from_bytes(data, byteorder="big"))
        self.record_time_info()
        #if len(self.rx_data) >= self.dump_size:
        self.data_dump_handler("GX " + str(self.rx_timestamps[-1].time()) + " " + data.decode("utf-8"))
        # print(data.decode("utf-8") + "\n")
        with open("gyrox_data.txt", "a") as f: # вставлено
            f.write(data.decode("utf-8") + "\n") # вставлено
        self.clear_lists()
    def accelY_notification_handler(self, sender: str, data: Any):
        if self.n_probes_ay > self.max_probes:
            return
        self.n_probes_ay += 1
        #self.rx_data.append(int.from_bytes(data, byteorder="big"))
        self.record_time_info()
        #if len(self.rx_data) >= self.dump_size:
        self.data_dump_handler("AY " + str(self.rx_timestamps[-1].time()) + " " + data.decode("utf-8"))
        # print(data.decode("utf-8") + "\n")
        with open("accely_data.txt", "a") as f: # вставлено
            f.write(data.decode("utf-8") + "\n") # вставлено
        self.clear_lists()

    def gyroY_notification_handler(self, sender: str, data: Any):
        if self.n_probes_gy > self.max_probes:
            return
        self.n_probes_gy += 1
        #self.rx_data.append(int.from_bytes(data, byteorder="big"))
        self.record_time_info()
        #if len(self.rx_data) >= self.dump_size:
        self.data_dump_handler("GY " + str(self.rx_timestamps[-1].time()) + " " + data.decode("utf-8"))
        # print(data.decode("utf-8") + "\n")
        with open("gyroy_data.txt", "a") as f: # вставлено
            f.write(data.decode("utf-8") + "\n") # вставлено
        self.clear_lists()
    def accelZ_notification_handler(self, sender: str, data: Any):
        if self.n_probes_az > self.max_probes:
            return
        self.n_probes_az += 1
        #self.rx_data.append(int.from_bytes(data, byteorder="big"))
        self.record_time_info()
        #if len(self.rx_data) >= self.dump_size:
        self.data_dump_handler("AZ " + str(self.rx_timestamps[-1].time()) + " " + data.decode("utf-8"))
        # print(data.decode("utf-8") + "\n")
        with open("accelz_data.txt", "a") as f: # вставлено
            f.write(data.decode("utf-8") + "\n") # вставлено
        self.clear_lists()

    def gyroZ_notification_handler(self, sender: str, data: Any):
        if self.n_probes_gz > self.max_probes:
            return
        self.n_probes_gz += 1
        #self.rx_data.append(int.from_bytes(data, byteorder="big"))
        self.record_time_info()
        #if len(self.rx_data) >= self.dump_size:
        self.data_dump_handler("GZ " + str(self.rx_timestamps[-1].time()) + " " + data.decode("utf-8"))
        # print(data.decode("utf-8") + "\n")
        with open("gyroz_data.txt", "a") as f: # вставлено
            f.write(data.decode("utf-8") + "\n") # вставлено
        self.clear_lists()


#############
# Loops
#############
async def user_console_manager(connection: Connection):
    print("In Connection loop")



async def main():
    while True:
        # YOUR APP CODE WOULD GO HERE.
        # await asyncio.sleep(0.5)
        pass

#############
# App Main
#############
# read_characteristic = "00001143-0000-1000-8000-00805f9b34fb"
write_characteristic = "00001142-0000-1000-8000-00805f9b34fb"
gyrox_characteristic = "3b18a65e-26c7-4c83-b8e2-bd11c06650ee"
accelx_characteristic = "84b8e0b2-9778-42de-89ea-0b44bb363c34"
gyroy_characteristic = "1dd4e426-0296-4535-8b20-fac505767d39"
accely_characteristic = "db8b6744-e800-40d3-8aec-e6b13ba851e8"
gyroz_characteristic = "0c1697bd-dc8e-4620-9a4e-9642012311d8"
accelz_characteristic = "b65eff6d-ff7f-45d6-b1b5-6c8b0e2f1770"

if __name__ == "__main__":

    # Create the event loop.
    loop = asyncio.get_event_loop()

    connection = Connection(
        loop, accelx_characteristic, gyrox_characteristic, accely_characteristic, gyroy_characteristic, accelz_characteristic, gyroz_characteristic, write_characteristic, print)

    try:
        asyncio.ensure_future(connection.manager())
        # asyncio.ensure_future(user_console_manager(connection))
        # asyncio.ensure_future(main())
        loop.run_forever()
    except KeyboardInterrupt:
        print()
        print("User stopped program.")
    finally:
        print("Disconnecting...")
        loop.run_until_complete(connection.cleanup())
