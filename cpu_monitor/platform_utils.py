import platform
import psutil

def get_cpu_temperature():
    system = platform.system()

    if system == "Windows":
        return get_windows_temp()
    elif system == "Linux":
        return get_linux_temp()
    elif system == "Darwin":
        return get_macos_temp()
    else:
        raise OSError(f"Unsupported operating system: {system}")

import platform
import psutil
import time

def get_cpu_temperature():
    system = platform.system()

    if system == "Windows":
        return get_windows_temp()
    elif system == "Linux":
        return get_linux_temp()
    elif system == "Darwin":
        return get_macos_temp()
    else:
        raise OSError(f"Unsupported operating system: {system}")

def get_windows_temp():
    import clr
    import os

    """Gets CPU temperature for Windows using Open Hardware Monitor Library"""
    try:
        file_path = os.path.join(os.getcwd(), 'OpenHardwareMonitorLib.dll')

        if not os.path.exists(file_path):
            return "OpenHardwareMonitorLib.dll not found in the specified location"

        clr.AddReference(file_path)

        from OpenHardwareMonitor import Hardware

        computer = Hardware.Computer()
        computer.CPUEnabled = True
        computer.MainboardEnabled = True
        computer.Open()
        
        all_temps = []

        for hardware in computer.Hardware:
            hardware.Update()

            for sensor in hardware.Sensors:
                if sensor.SensorType == Hardware.SensorType.Temperature:
                    if sensor.Value is not None:
                        all_temps.append(sensor.Value)
        
        if all_temps:
            temperature = all_temps[0]
            print(f"CPU Temperature: {temperature}°C")
            return temperature
        else:
            return "No valid temperature sensor data available"
    except Exception as e:
        return f"An error occurred while reading temperature: {str(e)}"

def get_linux_temp():    
    try:
        if hasattr(psutil, 'sensors_temperatures'):
            temps = psutil.sensors_temperatures()
            if "coretemp" in temps:
                return round(temps["coretemp"][0].current, 2)
            else:
                return "No temperature data available"
        else:
            return "sensors_temperatures not supported"
    except Exception as e:
        return f"Could not read temperature: {str(e)}"

def get_macos_temp():
    try:
        temp_output = os.popen("osx-cpu-temp").read().strip()
        return float(temp_output.split(' ')[0].replace('°C', ''))
    except Exception as e:
        return f"Could not read temperature: {str(e)}"

def get_linux_temp():    
    try:
        if hasattr(psutil, 'sensors_temperatures'):
            temps = psutil.sensors_temperatures()
            if "coretemp" in temps:
                return round(temps["coretemp"][0].current, 2)
            else:
                return "No temperature data available"
        else:
            return "sensors_temperatures not supported"
    except Exception as e:
        return f"Could not read temperature: {str(e)}"

def get_macos_temp():
    try:
        temp_output = os.popen("osx-cpu-temp").read().strip()
        return float(temp_output.split(' ')[0].replace('°C', ''))
    except Exception as e:
        return f"Could not read temperature: {str(e)}"
