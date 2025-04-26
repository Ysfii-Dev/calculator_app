import tkinter as tk
from tkinter import ttk
from ui.common_ui import CalculatorButton, Display


class TemperatureUI(tk.Frame):
    def __init__(self, master, converter, **kwargs):
        super().__init__(master, **kwargs)
        self.converter = converter

        # Create display frame
        self.display_frame = tk.Frame(self)
        self.display_frame.pack(fill=tk.BOTH, padx=5, pady=5)

        # Create temperature input fields
        self.create_temp_inputs()

        # Create keypad
        self.create_keypad()

        # Variable to track which field has focus
        self.active_scale = "celsius"  # Default
        self.is_updating = False  # Flag to prevent recursive updates

    def create_temp_inputs(self):
        # Labels for temperature scales
        scales = ["Celsius", "Fahrenheit", "Kelvin"]
        self.temp_vars = {}
        self.temp_entries = {}

        # Create entry fields for each temperature scale
        for i, scale in enumerate(scales):
            frame = tk.Frame(self.display_frame)
            frame.pack(fill=tk.X, pady=5)

            # Create label
            label = tk.Label(frame, text=f"{scale}:", width=10, anchor=tk.W)
            label.pack(side=tk.LEFT, padx=5)

            # Create entry field
            var = tk.StringVar()
            entry = tk.Entry(
                frame,
                textvariable=var,
                font=("Arial", 14),
                bd=3,
                relief=tk.SUNKEN,
                justify=tk.RIGHT
            )
            entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

            # Store variables and entries
            self.temp_vars[scale.lower()] = var
            self.temp_entries[scale.lower()] = entry

            # Add focus binding to track which entry is active
            entry.bind("<FocusIn>", lambda event, s=scale.lower()
                       : self.set_active_scale(s))

        # Create "Convert" button
        convert_btn = tk.Button(
            self.display_frame,
            text="Convert",
            command=self.convert_all,
            font=("Arial", 12, "bold"),
            bg="#99ccff",
            height=2
        )
        convert_btn.pack(fill=tk.X, padx=5, pady=10)

    def create_keypad(self):
        # Create keypad frame
        keypad_frame = tk.Frame(self)
        keypad_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Create buttons
        buttons = [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            ["±", "0", "."]
        ]

        for row_idx, row_buttons in enumerate(buttons):
            for col_idx, button_text in enumerate(row_buttons):
                if button_text == "±":
                    command = self.toggle_sign
                else:
                    def command(x=button_text): return self.append_digit(x)

                # Set color based on button type
                if button_text.isdigit():
                    bg = "#ffffff"
                else:
                    bg = "#f0f0f0"

                # Create button
                button = CalculatorButton(
                    keypad_frame,
                    text=button_text,
                    command=command,
                    bg=bg,
                    width=5,
                    height=3
                )
                button.grid(row=row_idx, column=col_idx,
                            padx=2, pady=2, sticky="nsew")

        # Create additional control buttons
        clear_btn = CalculatorButton(
            keypad_frame,
            text="C",
            command=self.clear_all,
            bg="#ff9999",
            width=5,
            height=3
        )
        clear_btn.grid(row=0, column=3, padx=2, pady=2, sticky="nsew")

        backspace_btn = CalculatorButton(
            keypad_frame,
            text="⌫",
            command=self.backspace,
            bg="#ffcc99",
            width=5,
            height=3
        )
        backspace_btn.grid(row=1, column=3, padx=2, pady=2, sticky="nsew")

        # Configure grid weights
        for i in range(4):  # Rows
            keypad_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):  # Columns
            keypad_frame.grid_columnconfigure(i, weight=1)

    def set_active_scale(self, scale):
        """Set which temperature scale is currently active"""
        self.active_scale = scale

    def append_digit(self, digit):
        """Add digit or decimal point to active entry"""
        # Get current value
        current = self.temp_vars[self.active_scale].get()

        # Check if we're trying to add another decimal point
        if digit == "." and "." in current:
            return

        # Append digit to active entry
        self.temp_vars[self.active_scale].set(current + digit)

    def toggle_sign(self):
        """Toggle sign of current value"""
        current = self.temp_vars[self.active_scale].get()
        if current:
            try:
                value = float(current)
                self.temp_vars[self.active_scale].set(str(-value))
            except ValueError:
                pass

    def backspace(self):
        """Remove last character from active entry"""
        current = self.temp_vars[self.active_scale].get()
        if current:
            self.temp_vars[self.active_scale].set(current[:-1])

    def clear_all(self):
        """Clear all temperature fields"""
        for var in self.temp_vars.values():
            var.set("")

    def convert_all(self):
        """Convert temperature from active scale to all other scales"""
        if self.is_updating:
            return

        self.is_updating = True
        try:
            # Get active scale and value
            scale = self.active_scale
            value_str = self.temp_vars[scale].get()

            if not value_str:
                # Clear all fields if active field is empty
                self.clear_all()
                return

            try:
                value = float(value_str)

                # Convert to all other scales
                for target_scale in self.temp_vars.keys():
                    if target_scale != scale:
                        converted = self.converter.convert(
                            value, scale, target_scale)
                        # Format to 2 decimal places
                        self.temp_vars[target_scale].set(f"{converted:.2f}")
            except ValueError:
                # Invalid input - clear other fields
                for target_scale in self.temp_vars.keys():
                    if target_scale != scale:
                        self.temp_vars[target_scale].set("")
        finally:
            self.is_updating = False
