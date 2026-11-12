import tkinter as tk
from tkinter import ttk, messagebox


# ==========================================
# 1. BASE CLASS: Dispositivo (SmartDevice)
# ==========================================
class SmartDevice:
    def __init__(self, name: str):
        self.name = name
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def status(self) -> str:
        """Polymorphic method to return current status description."""
        state_str = "ON" if self.is_on else "OFF"
        return f"[{self.name}] State: {state_str}"

    def configure(self, mode: str, intensity: int = None, scheduled_time: str = None) -> str:
        """
        Method demonstrating overload behavior using optional parameters:
        - configure(mode)
        - configure(mode, intensity)
        - configure(mode, intensity, scheduled_time)
        """
        config_summary = f"[{self.name}] Configured Mode: {mode}"
        if intensity is not None:
            config_summary += f" | Intensity/Level: {intensity}%"
        if scheduled_time is not None:
            config_summary += f" | Scheduled Time: {scheduled_time}"
        return config_summary


# ==========================================
# 2. CONCRETE CLASSES (Inheritance & Polymorphism)
# ==========================================
class SmartLight(SmartDevice):
    def __init__(self, name: str):
        super().__init__(name)
        self.brightness = 100

    def turn_on(self):
        super().turn_on()
        return f"Smart Light '{self.name}' illuminated."

    def turn_off(self):
        super().turn_off()
        return f"Smart Light '{self.name}' turned off."

    def status(self) -> str:
        base_status = super().status()
        return f"{base_status} | Brightness: {self.brightness}%"


class SmartBlind(SmartDevice):
    def __init__(self, name: str):
        super().__init__(name)
        self.open_percentage = 0

    def turn_on(self):
        super().turn_on()
        self.open_percentage = 100
        return f"Smart Blind '{self.name}' opened completely."

    def turn_off(self):
        super().turn_off()
        self.open_percentage = 0
        return f"Smart Blind '{self.name}' closed completely."

    def status(self) -> str:
        base_status = super().status()
        return f"{base_status} | Open Level: {self.open_percentage}%"


class SmartThermostat(SmartDevice):
    def __init__(self, name: str):
        super().__init__(name)
        self.temperature = 22  # default Celsius

    def turn_on(self):
        super().turn_on()
        return f"Smart Thermostat '{self.name}' climate control active."

    def turn_off(self):
        super().turn_off()
        return f"Smart Thermostat '{self.name}' climate control standby."

    def status(self) -> str:
        base_status = super().status()
        return f"{base_status} | Target Temp: {self.temperature}°C"


# ==========================================
# 3. CONTROL CLASS: Control Central (CentralControl)
# ==========================================
class CentralControl:
    def __init__(self):
        self.devices = []

    def add_device(self, device: SmartDevice):
        self.devices.append(device)

    def turn_on_all(self):
        logs = []
        for dev in self.devices:
            logs.append(dev.turn_on())
        return logs

    def turn_off_all(self):
        logs = []
        for dev in self.devices:
            logs.append(dev.turn_off())
        return logs

    def get_general_status(self):
        """Iterates over the list demonstrating polymorphism."""
        return [dev.status() for dev in self.devices]


# ==========================================
# 4. TKINTER GUI APPLICATION (English UI)
# ==========================================
class SmartHomeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Home Central Control - Phase 3")
        self.root.geometry("680x520")

        # Initialize Central Controller
        self.controller = CentralControl()
        self._populate_initial_devices()

        # Build UI Components
        self._create_widgets()
        self.update_status_display()

    def _populate_initial_devices(self):
        # Instantiate 3 sample devices
        self.controller.add_device(SmartLight("Living Room Light"))
        self.controller.add_device(SmartBlind("Bedroom Blind"))
        self.controller.add_device(SmartThermostat("Main Thermostat"))

    def _create_widgets(self):
        # Header
        header = ttk.Label(
            self.root, 
            text="Central Smart Device Management System", 
            font=("Helvetica", 14, "bold")
        )
        header.pack(pady=10)

        # Global Actions Frame
        global_frame = ttk.LabelFrame(self.root, text=" Global Actions ")
        global_frame.pack(fill="x", padx=15, pady=5)

        btn_on_all = ttk.Button(global_frame, text="Turn ON All", command=self.on_turn_on_all)
        btn_on_all.pack(side="left", padx=10, pady=10)

        btn_off_all = ttk.Button(global_frame, text="Turn OFF All", command=self.on_turn_off_all)
        btn_off_all.pack(side="left", padx=10, pady=10)

        btn_refresh = ttk.Button(global_frame, text="Refresh Status", command=self.update_status_display)
        btn_refresh.pack(side="left", padx=10, pady=10)

        # Individual Device Configuration Frame (Overload Demo)
        config_frame = ttk.LabelFrame(self.root, text=" Device Overloaded Configuration ")
        config_frame.pack(fill="x", padx=15, pady=5)

        ttk.Label(config_frame, text="Select Device:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.device_var = tk.StringVar()
        self.device_combo = ttk.Combobox(config_frame, textvariable=self.device_var, state="readonly")
        self.device_combo['values'] = [dev.name for dev in self.controller.devices]
        self.device_combo.current(0)
        self.device_combo.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(config_frame, text="Mode:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.entry_mode = ttk.Entry(config_frame, width=12)
        self.entry_mode.insert(0, "Eco")
        self.entry_mode.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(config_frame, text="Intensity (%):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_intensity = ttk.Entry(config_frame, width=12)
        self.entry_intensity.insert(0, "80")
        self.entry_intensity.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(config_frame, text="Time (HH:MM):").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.entry_time = ttk.Entry(config_frame, width=12)
        self.entry_time.insert(0, "20:00")
        self.entry_time.grid(row=1, column=3, padx=5, pady=5)

        btn_config = ttk.Button(config_frame, text="Apply Configuration", command=self.on_apply_config)
        btn_config.grid(row=2, column=0, columnspan=4, pady=8)

        # Console Display Frame
        console_frame = ttk.LabelFrame(self.root, text=" System Status & Logs ")
        console_frame.pack(fill="both", expand=True, padx=15, pady=5)

        self.txt_console = tk.Text(console_frame, wrap="word", height=10)
        self.txt_console.pack(fill="both", expand=True, padx=5, pady=5)

    def update_status_display(self):
        self.txt_console.delete("1.0", tk.END)
        self.txt_console.insert(tk.END, "=== GENERAL DEVICE STATUS ===\n")
        statuses = self.controller.get_general_status()
        for s in statuses:
            self.txt_console.insert(tk.END, f"• {s}\n")

    def on_turn_on_all(self):
        logs = self.controller.turn_on_all()
        self.update_status_display()
        self.txt_console.insert(tk.END, "\n=== ACTION LOGS ===\n")
        for log in logs:
            self.txt_console.insert(tk.END, f"-> {log}\n")

    def on_turn_off_all(self):
        logs = self.controller.turn_off_all()
        self.update_status_display()
        self.txt_console.insert(tk.END, "\n=== ACTION LOGS ===\n")
        for log in logs:
            self.txt_console.insert(tk.END, f"-> {log}\n")

    def on_apply_config(self):
        selected_name = self.device_var.get()
        mode = self.entry_mode.get().strip()
        intensity_raw = self.entry_intensity.get().strip()
        time_raw = self.entry_time.get().strip()

        # Find target device
        target_dev = next((d for d in self.controller.devices if d.name == selected_name), None)

        if target_dev:
            intensity = int(intensity_raw) if intensity_raw.isdigit() else None
            scheduled_time = time_raw if len(time_raw) > 0 else None

            # Execute overloaded method
            result = target_dev.configure(mode, intensity, scheduled_time)
            messagebox.showinfo("Configuration Applied", result)
            self.update_status_display()


# ==========================================
# MAIN ENTRY POINT
# ==========================================
if __name__ == "__main__":
    root = tk.Tk()
    app = SmartHomeApp(root)
    root.mainloop()
    