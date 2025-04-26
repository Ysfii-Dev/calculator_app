class ScientificCalculator:
    def __init__(self):
        self.memory = 0
        self.angle_mode = "DEG"  # Default: DEG (bisa diubah ke RAD)

    def set_angle_mode(self, mode):
        """Set angle mode to DEG or RAD"""
        if mode in ["DEG", "RAD"]:
            self.angle_mode = mode
        else:
            raise ValueError("Mode must be 'DEG' or 'RAD'")

    def get_angle_mode(self):
        """Get current angle mode"""
        return self.angle_mode

    def to_radians(self, angle):
        """Convert angle to radians if needed"""
        import math
        if self.angle_mode == "DEG":
            return math.radians(angle)
        return angle

    def to_degrees(self, angle):
        """Convert angle to degrees if needed"""
        import math
        if self.angle_mode == "RAD":
            return math.degrees(angle)
        return angle

    # Basic operations
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    # Trigonometric functions
    def sin(self, angle):
        import math
        return math.sin(self.to_radians(angle))

    def cos(self, angle):
        import math
        return math.cos(self.to_radians(angle))

    def tan(self, angle):
        import math
        return math.tan(self.to_radians(angle))

    def arcsin(self, value):
        import math
        result = math.asin(value)
        return self.to_degrees(result) if self.angle_mode == "DEG" else result

    def arccos(self, value):
        import math
        result = math.acos(value)
        return self.to_degrees(result) if self.angle_mode == "DEG" else result

    def arctan(self, value):
        import math
        result = math.atan(value)
        return self.to_degrees(result) if self.angle_mode == "DEG" else result

    # Logarithmic functions
    def log10(self, value):
        import math
        if value <= 0:
            raise ValueError("Log input must be positive")
        return math.log10(value)

    def ln(self, value):
        import math
        if value <= 0:
            raise ValueError("Ln input must be positive")
        return math.log(value)

    # Exponential functions
    def power(self, base, exponent):
        return base ** exponent

    def square(self, value):
        return value ** 2

    def sqrt(self, value):
        import math
        if value < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(value)

    def nth_root(self, value, n):
        if n == 0:
            raise ValueError("Root index cannot be zero")
        if value < 0 and n % 2 == 0:
            raise ValueError("Cannot calculate even root of negative number")
        return value ** (1/n)

    # Additional functions
    def factorial(self, n):
        import math
        if n < 0 or not isinstance(n, int):
            raise ValueError("Factorial requires a non-negative integer")
        return math.factorial(n)

    def percent(self, value):
        return value / 100

    def inverse(self, value):
        if value == 0:
            raise ValueError("Cannot calculate inverse of zero")
        return 1 / value

    # Memory functions
    def memory_store(self, value):
        self.memory = value

    def memory_recall(self):
        return self.memory

    def memory_clear(self):
        self.memory = 0

    def memory_add(self, value):
        self.memory += value

    def memory_subtract(self, value):
        self.memory -= value
