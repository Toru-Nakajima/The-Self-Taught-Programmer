import math

class Circle():
    def __init__(self, diameter):
        self.diameter = diameter

    def area(self):
        return (math.pi / 4 ) * self.diameter ** 2


circle01 =  Circle(4)
print(circle01.area())


