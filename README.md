# Temp Reader

This is a Python-based application that monitors and displays the CPU temperature of your system in real time. The application uses OpenHardwareMonitor library for fetching temperature data and displays the information via a simple graphical user interface (GUI) built with Tkinter.

## Features

Real-time CPU Temperature Monitoring: Continuously displays the current CPU temperature in a simple graphical window.
Cross-platform Support: Detects and displays CPU temperature on Windows, Linux, and macOS (depending on available sensors).
OpenHardwareMonitor Integration: Uses OpenHardwareMonitor's API to retrieve temperature data on Windows.

## Prerequisites

Python 3.x: Ensure you have Python 3.x installed on your system.

Required Python Packages:
    pythonnet (for integrating with OpenHardwareMonitor on Windows)
    psutil (for reading sensor data on Linux)
    tkinter (usually included with Python, for the GUI)

You can install the required packages by running the following command:

    pip install pythonnet psutil

## Installation

    git clone https://github.com/razvanpetrascu/temp-reader.git
    cd temp-reader

## Unblock OpenHardwareMonitor DLL:

Ensure the OpenHardwareMonitorLib.dll is unblocked (Windows: right click -> properties -> Unblock) and in the root directory of the project. You can download this file directly from the [OpenHardwareMonitor](https://openhardwaremonitor.org).

## Install Dependencies: Install the required Python dependencies using pip:

    pip install -r requirements.txt

## Usage

Run Visual Studio Code (or whatever IDE you're using) **as Administrator**.

Start the app by running the main.py script:

>python main.py

User Interface:
A GUI window will open, displaying the detected CPU name and real-time CPU temperature.
The temperature will be updated automatically every 0.2 seconds.
The console will also log the CPU temperature at regular intervals.

Manual Refresh:
    ~~You can manually refresh the temperature reading by clicking the "Refresh" button in the GUI.~~

## Supported Platforms

Windows
Linux (*not tested*)
macOS (*not tested*)

## Known Issues

Windows: OpenHardwareMonitor **might** need to be running in the background for temperature readings to work.
Linux and macOS: May not work on all devices due to limitations in sensor availability or command tools.

## Screenshots
![Alt text](/assets/gui.jpg?raw=true)
![Alt text](/assets/console-logs.jpg?raw=true)

## License

This project is free to use.

## Feel free to submit issues or pull requests to improve the application. Contributions are welcome!
Author

Razvan Petrascu - https://github.com/razvanpetrascu

