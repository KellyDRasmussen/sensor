# Raspberry Pi Sensor

This project utilizes a Raspberry Pi and a BME680 sensor to collect environmental data such as temperature, humidity, gas resistance, and air pressure. The data is then uploaded to Adafruit IO, allowing for real-time monitoring and analysis.

## Features

- **Temperature Monitoring**: Capture ambient temperature data.
- **Humidity Tracking**: Monitor the relative humidity of the environment.
- **Gas Resistance Detection**: Measure gas resistance as an indicator of air quality.
- **Air Pressure Sensing**: Record barometric pressure changes.
- **Real-Time Data Upload**: Data is uploaded continuously to Adafruit IO for live monitoring.

## Getting Started

Follow these instructions to set up the project on your local machine for development and operational purposes.

### Prerequisites

You need to have a Raspberry Pi set up with internet connectivity. Additionally, install the necessary libraries for interacting with the BME680 sensor and Adafruit IO:

### Installation

1. **Clone the Repository**:
   Clone this repository to your Raspberry Pi using:
   
   git clone https://github.com/KellyDRasmussen/sensor.git
   
2. **Set up Adafruit IO**:
   - Create an account at [Adafruit IO](https://io.adafruit.com/).
   - Create feeds for temperature, humidity, gas resistance, and pressure.
   - Obtain your Adafruit IO username and active key.

3. **Environment Configuration**:
   Set your Adafruit IO credentials and feed names as environment variables:
   ```bash
   export ADAFRUIT_IO_USERNAME='your_username'
   export ADAFRUIT_IO_KEY='your_key'
   ```

## Credits and Acknowledgments

- **Adafruit Industries** for providing the Adafruit IO platform and Python libraries.
- **Pimoroni** for their BME680 Python library, used to interface with the sensor.

