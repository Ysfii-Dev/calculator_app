class TemperatureConverter:
    def __init__(self):
        pass

    def celsius_to_fahrenheit(self, celsius):
        """Convert Celsius to Fahrenheit"""
        return (celsius * 9/5) + 32

    def celsius_to_kelvin(self, celsius):
        """Convert Celsius to Kelvin"""
        return celsius + 273.15

    def fahrenheit_to_celsius(self, fahrenheit):
        """Convert Fahrenheit to Celsius"""
        return (fahrenheit - 32) * 5/9

    def fahrenheit_to_kelvin(self, fahrenheit):
        """Convert Fahrenheit to Kelvin"""
        celsius = self.fahrenheit_to_celsius(fahrenheit)
        return self.celsius_to_kelvin(celsius)

    def kelvin_to_celsius(self, kelvin):
        """Convert Kelvin to Celsius"""
        return kelvin - 273.15

    def kelvin_to_fahrenheit(self, kelvin):
        """Convert Kelvin to Fahrenheit"""
        celsius = self.kelvin_to_celsius(kelvin)
        return self.celsius_to_fahrenheit(celsius)

    def convert(self, value, from_unit, to_unit):
        """
        Convert temperature between units

        Parameters:
        - value: temperature value to convert
        - from_unit: source unit ('celsius', 'fahrenheit', or 'kelvin')
        - to_unit: target unit ('celsius', 'fahrenheit', or 'kelvin')

        Returns:
        - Converted temperature value
        """
        # Standardize unit names to lowercase
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        # Check if units are valid
        valid_units = ['celsius', 'fahrenheit', 'kelvin']
        if from_unit not in valid_units or to_unit not in valid_units:
            raise ValueError(
                "Units must be 'celsius', 'fahrenheit', or 'kelvin'")

        # If source and target units are the same, return the original value
        if from_unit == to_unit:
            return value

        # Convert from source unit to target unit
        if from_unit == 'celsius':
            if to_unit == 'fahrenheit':
                return self.celsius_to_fahrenheit(value)
            elif to_unit == 'kelvin':
                return self.celsius_to_kelvin(value)

        elif from_unit == 'fahrenheit':
            if to_unit == 'celsius':
                return self.fahrenheit_to_celsius(value)
            elif to_unit == 'kelvin':
                return self.fahrenheit_to_kelvin(value)

        elif from_unit == 'kelvin':
            if to_unit == 'celsius':
                return self.kelvin_to_celsius(value)
            elif to_unit == 'fahrenheit':
                return self.kelvin_to_fahrenheit(value)
