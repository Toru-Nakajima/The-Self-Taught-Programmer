class Square():
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 4

    def change_size(self, new_size):
        self.side += new_size



a_square = Square(50)
print(a_square.side)
print(a_square.calculate_perimeter())


a_square.change_size(5)
print(a_square.side)
print(a_square.calculate_perimeter())

a_square.change_size(-10)
print(a_square.side)
print(a_square.calculate_perimeter())

