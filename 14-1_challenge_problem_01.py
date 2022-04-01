class Square():
    square_list = []

    def __init__(self, s):
        self.side = s
        self.square_list.append((self.side))



square01 = Square(50)
print(Square.square_list)
square02 = Square(100)
print(Square.square_list)
square03 = Square(150)
print(Square.square_list)

