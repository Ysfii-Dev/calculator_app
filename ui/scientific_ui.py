import tkinter as tk
from tkinter import ttk
from ui.common_ui import CalculatorButton, Display


class ScientificUI(tk.Frame):
    def __init__(self, master, calculator, **kwargs):
        super().__init__(master, **kwargs)
        self.calculator = calculator
        self.current_expression = ""
        self.last_result = 0

        # Create display
        self.display = Display(self)
        self.display.pack(fill=tk.X, padx=5, pady=5)

        # Create angle mode selector
        self.create_angle_mode_selector()

        # Create buttons frame
        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Create buttons
        self.create_buttons()

    def create_angle_mode_selector(self):
        frame = tk.Frame(self)
        frame.pack(fill=tk.X, padx=5, pady=5)

        self.angle_var = tk.StringVar()
        self.angle_var.set("DEG")  # Default

        # Add radio buttons
        deg_rb = tk.Radiobutton(
            frame,
            text="DEG",
            variable=self.angle_var,
            value="DEG",
            command=self.toggle_angle_mode,
            indicatoron=False,
            width=10
        )
        deg_rb.pack(side=tk.LEFT, expand=True)

        rad_rb = tk.Radiobutton(
            frame,
            text="RAD",
            variable=self.angle_var,
            value="RAD",
            command=self.toggle_angle_mode,
            indicatoron=False,
            width=10
        )
        rad_rb.pack(side=tk.LEFT, expand=True)

    def toggle_angle_mode(self):
        mode = self.angle_var.get()
        self.calculator.set_angle_mode(mode)

    def create_buttons(self):
        # Define button layout with rows and columns
        buttons = [
            # Row 1
            [
                {"text": "MC", "command": self.memory_clear, "bg": "#e0e0e0"},
                {"text": "MR", "command": self.memory_recall, "bg": "#e0e0e0"},
                {"text": "M+", "command": self.memory_add, "bg": "#e0e0e0"},
                {"text": "M-", "command": self.memory_subtract, "bg": "#e0e0e0"},
                {"text": "MS", "command": self.memory_store, "bg": "#e0e0e0"}
            ],
            # Row 2
            [
                {"text": "x²", "command": lambda: self.calculate_function(
                    'square')},
                {"text": "x³",
                    "command": lambda: self.append_operation("**3")},
                {"text": "xⁿ", "command": lambda: self.append_operation("**")},
                {"text": "eˣ",
                    "command": lambda: self.calculate_function('exp')},
                {"text": "10ˣ",
                    "command": lambda: self.append_operation("10**")}
            ],
            # Row 3
            [
                {"text": "1/x",
                    "command": lambda: self.calculate_function('inverse')},
                {"text": "²√x",
                    "command": lambda: self.calculate_function('sqrt')},
                {"text": "³√x", "command": lambda: self.append_operation(
                    "**(1/3)")},
                {"text": "ⁿ√x", "command": lambda: self.append_operation(
                    "**(1/")},
                {"text": "ln",
                    "command": lambda: self.calculate_function('ln')}
            ],
            # Row 4
            [
                {"text": "x!", "command": lambda: self.calculate_function(
                    'factorial')},
                {"text": "sin",
                    "command": lambda: self.calculate_function('sin')},
                {"text": "cos",
                    "command": lambda: self.calculate_function('cos')},
                {"text": "tan",
                    "command": lambda: self.calculate_function('tan')},
                {"text": "log",
                    "command": lambda: self.calculate_function('log10')}
            ],
            # Row 5
            [
                {"text": "π", "command": lambda: self.append_text(
                    "3.14159265359")},
                {"text": "e", "command": lambda: self.append_text(
                    "2.71828182846")},
                {"text": "(", "command": lambda: self.append_text("(")},
                {"text": ")", "command": lambda: self.append_text(")")},
                {"text": "n!", "command": lambda: self.calculate_function(
                    'factorial')}
            ],
            # Row 6
            [
                {"text": "C", "command": self.clear, "bg": "#ff9999"},
                {"text": "⌫", "command": self.backspace, "bg": "#ffcc99"},
                {"text": "%", "command": lambda: self.append_operation("%")},
                {"text": "÷", "command": lambda: self.append_operation(
                    "/"), "bg": "#99ccff"}
            ],
            # Row 7
            [
                {"text": "7", "command": lambda: self.append_text("7")},
                {"text": "8", "command": lambda: self.append_text("8")},
                {"text": "9", "command": lambda: self.append_text("9")},
                {"text": "×", "command": lambda: self.append_operation(
                    "*"), "bg": "#99ccff"}
            ],
            # Row 8
            [
                {"text": "4", "command": lambda: self.append_text("4")},
                {"text": "5", "command": lambda: self.append_text("5")},
                {"text": "6", "command": lambda: self.append_text("6")},
                {"text": "-",
                    "command": lambda: self.append_operation("-"), "bg": "#99ccff"}
            ],
            # Row 9
            [
                {"text": "1", "command": lambda: self.append_text("1")},
                {"text": "2", "command": lambda: self.append_text("2")},
                {"text": "3", "command": lambda: self.append_text("3")},
                {"text": "+",
                    "command": lambda: self.append_operation("+"), "bg": "#99ccff"}
            ],
            # Row 10
            [
                {"text": "±", "command": self.toggle_sign},
                {"text": "0", "command": lambda: self.append_text("0")},
                {"text": ".", "command": lambda: self.append_text(".")},
                {"text": "=", "command": self.calculate, "bg": "#66cc66"}
            ]
        ]

        # Create all buttons
        for row_idx, row_buttons in enumerate(buttons):
            for col_idx, button_config in enumerate(row_buttons):
                # Default color for number buttons
                if "bg" not in button_config:
                    if button_config["text"].isdigit():
                        button_config["bg"] = "#ffffff"
                    else:
                        button_config["bg"] = "#f0f0f0"

                # Last row spans multiple columns
                # Last column
                if row_idx >= 6 and col_idx == len(row_buttons) - 1:
                    col_span = 1
                else:
                    col_span = 1

                # Create button
                button = CalculatorButton(
                    self.buttons_frame,
                    text=button_config["text"],
                    command=button_config["command"],
                    bg=button_config["bg"]
                )
                button.grid(row=row_idx, column=col_idx, padx=2,
                            pady=2, sticky="nsew", columnspan=col_span)

        # Configure grid weights
        for i in range(10):  # Rows
            self.buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(5):  # Columns
            self.buttons_frame.grid_columnconfigure(i, weight=1)

    def append_text(self, text):
        self.display.append_text(text)

    def append_operation(self, op):
        current_text = self.display.get_text()
        if current_text:
            self.display.set_text(current_text + op)
        elif op in ["+", "-"]:  # Allow starting with + or -
            self.display.set_text(op)

    def clear(self):
        self.display.clear_all()
        self.current_expression = ""

    def backspace(self):
        current_text = self.display.get_text()
        if current_text:
            self.display.set_text(current_text[:-1])

    def toggle_sign(self):
        current_text = self.display.get_text()
        if current_text:
            try:
                value = float(current_text)
                self.display.set_text(str(-value))
            except ValueError:
                pass  # Not a simple number

    def calculate(self):
        expression = self.display.get_text()
        if expression:
            try:
                # Replace % operator with /100
                expression = expression.replace("%", "/100")

                # Evaluate the expression
                result = eval(expression)

                # Update history
                self.display.set_history(expression)

                # Update display with result
                self.display.set_text(str(result))
                self.last_result = result
            except Exception as e:
                self.display.set_text("Error")
                print(f"Calculation error: {e}")

    def calculate_function(self, func_name):
        current_text = self.display.get_text()
        if current_text:
            try:
                # Try to convert to number
                value = float(eval(current_text))

                # Apply the function
                if func_name == 'square':
                    result = self.calculator.square(value)
                elif func_name == 'sqrt':
                    result = self.calculator.sqrt(value)
                elif func_name == 'sin':
                    result = self.calculator.sin(value)
                elif func_name == 'cos':
                    result = self.calculator.cos(value)
                elif func_name == 'tan':
                    result = self.calculator.tan(value)
                elif func_name == 'log10':
                    result = self.calculator.log10(value)
                elif func_name == 'ln':
                    result = self.calculator.ln(value)
                elif func_name == 'factorial':
                    result = self.calculator.factorial(int(value))
                elif func_name == 'inverse':
                    result = self.calculator.inverse(value)
                elif func_name == 'exp':
                    import math
                    result = math.exp(value)
                else:
                    result = value

                # Update history
                self.display.set_history(f"{func_name}({current_text})")

                # Update display
                self.display.set_text(str(result))
                self.last_result = result
            except Exception as e:
                self.display.set_text("Error")
                print(f"Function calculation error: {e}")

    def memory_clear(self):
        self.calculator.memory_clear()

    def memory_recall(self):
        value = self.calculator.memory_recall()
        self.display.set_text(str(value))

    def memory_add(self):
        try:
            value = float(eval(self.display.get_text()))
            self.calculator.memory_add(value)
        except:
            pass

    def memory_subtract(self):
        try:
            value = float(eval(self.display.get_text()))
            self.calculator.memory_subtract(value)
        except:
            pass

    def memory_store(self):
        try:
            value = float(eval(self.display.get_text()))
            self.calculator.memory_store(value)
        except:
            pass
