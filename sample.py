class Point:

    def __init__(self, x, y):
        print('INside init')
        self.x = x
        self.y = y

    def __add__(self, other):
        print('INside add')
        print('This is self', self.x)
        print('This is other', other.x)
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        print('INside str')
        return f"{self.x}, {self.y}"


point = Point(1, 2)
other = Point(10, 20)
another = Point(20, 30)
print(point + other + another)
