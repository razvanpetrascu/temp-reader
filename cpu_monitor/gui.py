import tkinter as tk
from cpu_monitor.core import get_cpu_temperature_reading, get_cpu_name

class TemperatureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TempReader")
        self.root.geometry("250x70")

        # Create labels for hardware and temperature
        self.cpu_name = get_cpu_name()

        self.hardware_label = tk.Label(root, text=f"{self.cpu_name}", font=("Arial", 14))
        self.hardware_label.pack(pady=1)

        self.temp_label = tk.Label(root, text="Temp: ", font=("Arial", 14))
        self.temp_label.pack(pady=1)

        # Button to manually refresh
        #self.refresh_button = tk.Button(root, text="Refresh", command=self.update_temperature)
        #self.refresh_button.pack(pady=20)

        self.update_temperature()

    def update_temperature(self):
        temp_info = get_cpu_temperature_reading()

        self.temp_label.config(text=f"{temp_info}°C")

        # Timer to update temperature periodically
        self.root.after(200, self.update_temperature)

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureApp(root)
    root.mainloop()
