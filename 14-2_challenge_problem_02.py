class Square():
    square_list = []

    def __init__(self, s):
        self.side = s
        self.square_list.append((self.side))

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side, self.side, self.side, self.side)



square01 = Square(50)
square02 = Square(100)
square03 = Square(150)


print(square01)
print(square02)
print(square03)

