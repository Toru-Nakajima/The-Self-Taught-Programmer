class Rectangle():
    def __init__(self, l, d):
        self.length = l
        self.width = d

rectangle01 = Rectangle(10, 10)
rectangle02 = Rectangle(10, 50)


print(rectangle01.length is rectangle01.width)
print(rectangle02.length is rectangle02.width)

