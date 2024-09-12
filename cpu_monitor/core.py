from cpu_monitor.platform_utils import get_cpu_temperature

def get_cpu_temperature_reading():
    temp = get_cpu_temperature()
    return f"CPU Temperature: {temp}"

def get_cpu_name():
    import clr
    import os

    try:
        # Path to the OpenHardwareMonitorLib.dll
        file_path = os.path.join(os.getcwd(), 'OpenHardwareMonitorLib.dll')

        clr.AddReference(file_path)
        from OpenHardwareMonitor import Hardware

        # Initialize OpenHardwareMonitor
        computer = Hardware.Computer()
        computer.CPUEnabled = True
        computer.Open()

        for hardware in computer.Hardware:
            if hardware.HardwareType == Hardware.HardwareType.CPU:
                return hardware.Name  # Return the name of the CPU

        return "Unknown CPU"
    except Exception as e:
        return f"Error reading CPU name: {str(e)}"
