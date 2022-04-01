class Triangle():
    def __init__(self, base_side, hight):
        self.base_side = base_side
        self.hight = hight

    def calculate_area(self):
        return self.base_side * self.hight / 2


triangle01 =  Triangle(4, 4)
print(triangle01.calculate_area())


