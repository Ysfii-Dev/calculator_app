import tkinter as tk
from tkinter import ttk

from scientific_calc import ScientificCalculator
from temp_converter import TemperatureConverter
from ui.scientific_ui import ScientificUI
from ui.temperature_ui import TemperatureUI
from ui.common_ui import ModeSwitcher


class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Calculator")
        self.geometry("400x600")
        self.minsize(320, 500)
        self.configure(bg="#f0f0f0")

        # Initialize calculator modules
        self.scientific_calc = ScientificCalculator()
        self.temp_converter = TemperatureConverter()

        # Create main frame
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Create mode switcher
        self.mode_switcher = ModeSwitcher(
            self.main_frame,
            modes=["Scientific", "Temperature"],
            command=self.switch_mode
        )
        self.mode_switcher.pack(fill=tk.X, padx=5, pady=5)

        # Create frame for calculator UI
        self.calculator_frame = tk.Frame(self.main_frame)
        self.calculator_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Create calculator UIs
        self.scientific_ui = ScientificUI(
            self.calculator_frame, self.scientific_calc)
        self.temperature_ui = TemperatureUI(
            self.calculator_frame, self.temp_converter)

        # Set default mode
        self.current_mode = "Scientific"
        self.scientific_ui.pack(fill=tk.BOTH, expand=True)

        # Add status bar
        self.status_bar = tk.Label(
            self,
            text="Ready",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def switch_mode(self):
        """Switch between Scientific and Temperature modes"""
        new_mode = self.mode_switcher.get_mode()

        if new_mode != self.current_mode:
            # Hide current UI
            if self.current_mode == "Scientific":
                self.scientific_ui.pack_forget()
            else:
                self.temperature_ui.pack_forget()

            # Show new UI
            if new_mode == "Scientific":
                self.scientific_ui.pack(fill=tk.BOTH, expand=True)
                self.status_bar.config(text="Scientific Calculator Mode")
            else:
                self.temperature_ui.pack(fill=tk.BOTH, expand=True)
                self.status_bar.config(text="Temperature Converter Mode")

            # Update current mode
            self.current_mode = new_mode


if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
