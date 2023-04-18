class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Jestem prostokątem'

    def area(self):
        return  self.a * self.b

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)
        self.a = a
        self.b = a

    def __str__(self):
        return 'Jestem kwadratem'

class Cube(Square):
    def cube_area(self):
        return 6 * super().area()

    def __str__(self):
        return 'Jestem szescianem'

moj_prostoka = Rectangle(2, 5)
print(moj_prostoka, 'moje pole to: ', moj_prostoka.area())

moj_kwadrat = Square(5)
print(moj_kwadrat, 'moje pole to: ', moj_kwadrat.area())

moj_szescian = Cube(4)
print(moj_szescian, 'moje pole to: ', moj_szescian.cube_area())

