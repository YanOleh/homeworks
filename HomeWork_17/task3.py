from math import gcd
'''   (+, -, /, *)   '''
class Fraction:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def simplify(self):
        simpl = gcd(self.x, self.y)
        self.x //= simpl
        self.y //= simpl
    def __add__(self, other):    #  +
        if isinstance(other, Fraction):
            new_x = self.x * other.y + other.x * self.y
            new_y = self.y * other.y
            return Fraction(new_x, new_y)
        else:
            raise TypeError


    def __sub__(self, other):   #  -
        if isinstance(other, Fraction):
            new_x = self.x * other.y - other.x * self.y
            new_y = self.y * other.y
            return Fraction(new_x, new_y)
        else:
            raise TypeError

    def __truediv__(self, other):    #  /
        if other.x == 0:
            raise ValueError("Cannot divide by zero")
        if isinstance(other, Fraction):
            new_x = self.x * other.y
            new_y = self.y * other.x
            return Fraction(new_x, new_y)
        else:
            raise TypeError



    def __mul__(self, other):    #  *
        if isinstance(other, Fraction):
            new_x = self.x * other.x
            new_y = self.y * other.y
            return Fraction(new_x, new_y)
        else:
            raise TypeError

    def __eq__(self, other):
        if isinstance(other, Fraction):
            self.simplify()
            other.simplify()
            return self.x == other.x and self.y == other.y
        else:
            raise TypeError

    def __repr__(self):
        return f"Fraction({self.x}, {self.y})"
    def __str__(self):
        self.simplify()
        return f"{self.x}/{self.y}"


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)

    print((x + y) == Fraction(3, 4))