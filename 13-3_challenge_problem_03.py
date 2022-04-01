class Shape():
    def what_am_i(self):
        print("I am shape.")



class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return self.width * 2 + self.length *2


class Square(Shape):
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 4



a_rectangle = Rectangle(25, 50)
a_square = Square(50)

print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())

a_rectangle.what_am_i()
a_square.what_am_i()

