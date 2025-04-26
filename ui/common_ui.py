import tkinter as tk
from tkinter import ttk


class CalculatorButton(tk.Button):
    """Custom button for calculator with consistent styling"""

    def __init__(self, master, text, command=None, width=5, height=2, bg="#f0f0f0", **kwargs):
        super().__init__(
            master,
            text=text,
            command=command,
            width=width,
            height=height,
            font=("Arial", 10),
            bg=bg,
            relief=tk.RAISED,
            bd=2,
            **kwargs
        )


class Display(tk.Frame):
    """Display frame for calculator results"""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Create entry widget for display
        self.display_var = tk.StringVar()
        self.display = tk.Entry(
            self,
            textvariable=self.display_var,
            font=("Arial", 20),
            bd=5,
            relief=tk.SUNKEN,
            justify=tk.RIGHT
        )
        self.display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Small label to show operation history
        self.history_var = tk.StringVar()
        self.history = tk.Label(
            self,
            textvariable=self.history_var,
            font=("Arial", 10),
            anchor=tk.E
        )
        self.history.pack(fill=tk.X, padx=5, pady=(0, 5))

    def set_text(self, text):
        """Set display text"""
        self.display_var.set(text)

    def get_text(self):
        """Get display text"""
        return self.display_var.get()

    def append_text(self, text):
        """Append text to display"""
        current = self.display_var.get()
        self.display_var.set(current + text)

    def set_history(self, text):
        """Set history text"""
        self.history_var.set(text)

    def clear(self):
        """Clear display"""
        self.display_var.set("")

    def clear_history(self):
        """Clear history"""
        self.history_var.set("")

    def clear_all(self):
        """Clear both display and history"""
        self.clear()
        self.clear_history()


class ModeSwitcher(tk.Frame):
    """Frame for switching between calculator modes"""

    def __init__(self, master, modes, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.mode_var = tk.StringVar()
        self.mode_var.set(modes[0])  # Set default mode

        # Create radio buttons for each mode
        for i, mode in enumerate(modes):
            rb = tk.Radiobutton(
                self,
                text=mode,
                variable=self.mode_var,
                value=mode,
                command=command,
                indicatoron=False,
                width=15,
                font=("Arial", 10),
                relief=tk.RAISED,
                bd=2
            )
            rb.grid(row=0, column=i, padx=2, pady=5, sticky="we")

    def get_mode(self):
        """Get current mode"""
        return self.mode_var.get()

    def set_mode(self, mode):
        """Set mode"""
        self.mode_var.set(mode)
