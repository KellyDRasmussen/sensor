#!/usr/bin/env python

import time
import bme680
from Adafruit_IO import Client, RequestError

# Adafruit IO credentials
ADAFRUIT_IO_USERNAME = 'your_username'
ADAFRUIT_IO_KEY = 'your_adafruit_io_key'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

print("""temperature-pressure-humidity.py - Displays temperature, pressure, and humidity.
If you don't need gas readings, then you can read temperature,
pressure, and humidity quickly.
Press Ctrl+C to exit
""")

try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except (RuntimeError, IOError):
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

# Sensor oversampling settings
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

print('Polling:')
try:
    while True:
        if sensor.get_sensor_data():
            temp = sensor.data.temperature
            pressure = sensor.data.pressure
            humidity = sensor.data.humidity
            output = '{0:.2f} C, {1:.2f} hPa, {2:.3f} %RH'.format(temp, pressure, humidity)
            print(output)
            try:
                # Send data to Adafruit IO using specific feed keys
                aio.send_data('temperature-feed', temp)
                aio.send_data('pressure-feed', pressure)
                aio.send_data('humidity-feed', humidity)
            except RequestError as e:
                print('Failed to send data to Adafruit IO:', e)
        time.sleep(10)  # Upload interval; adjust as needed

except KeyboardInterrupt:
    print("Script stopped by user.")
