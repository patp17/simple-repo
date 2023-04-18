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

# class Cube(Square):
#     def cube_area(self):
#         return 6 * super().area()
#
#     def __str__(self):
#         return 'Jestem szescianem'
#
#     def cube_volume(self):
#         return super().area() * self.a

class Cuboid():
    def __init__(self, figure, height):
        self.base = figure
        self.height = height

    def volume(self):
        return self.base.area() * self.height


moj_prostoka = Rectangle(2, 5)
print(moj_prostoka, 'moje pole to: ', moj_prostoka.area())

moj_kwadrat = Square(5)
print(moj_kwadrat, 'moje pole to: ', moj_kwadrat.area())

# moj_szescian = Cube(4)
# print(moj_szescian, 'moje pole to: ', moj_szescian.cube_area())
#
# print(moj_szescian, 'moja objetosx to: ', moj_szescian.cube_volume())
moj_szescian = Cuboid((Square(5)), 2)
print('Objetosc szescianu wynosi: ', moj_szescian.volume())

moj_prostopadloscian = Cuboid((Rectangle(5, 4)), 2)
print('Objetosc prostopadloscian wynosi: ', moj_prostopadloscian.volume())

