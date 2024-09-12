from cpu_monitor.gui import TemperatureApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureApp(root)
    root.mainloop()
