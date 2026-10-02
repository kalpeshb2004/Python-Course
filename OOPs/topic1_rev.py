# Code: Temperature class bana. celsius property + fahrenheit computed read-only property. Celsius < -273.15 → ValueError.

class Temperature():
    def __init__(self,celcius):
        self._celsius = celcius

    @property
    def celcius(self):
        return self._celcius

    @celcius.setter
    def celcius(self,fahrenheit):
        if fahrenheit < -273.15:
            raise ValueError("valueError")
        self._celcius = fahrenheit

    @celcius.deleter
    def celcius(self):
        del self._celcius

p1 = Temperature(100)
p1.celcius(200)
print(p1.celcius)
p1.celcius(-300)
