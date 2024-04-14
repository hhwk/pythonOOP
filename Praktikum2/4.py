import math

class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

r = 7
circle = Circle(r)
circle_area = circle.calculate_area()
circle_perimeter = circle.calculate_perimeter()
print("Круг:")
print("Радиус:", r)
print("Площадь:", circle_area)
print("Периметр:", circle_perimeter)

length = 5
width = 10
rectangle = Rectangle(length, width)
rectangle_area = rectangle.calculate_area()
rectangle_perimeter = rectangle.calculate_perimeter()
print("\nПрямоугольник:")
print("Длина:", length)
print("Ширина:", width)
print("Площадь:", rectangle_area)
print("Периметр:", rectangle_perimeter)

base = 5
height = 8
side1 = 3
side2 = 4
side3 = 6
triangle = Triangle(base, height, side1, side2, side3)
triangle_area = triangle.calculate_area()
triangle_perimeter = triangle.calculate_perimeter()
print("\nТреугольник:")
print("Основание:", base)
print("Высота:", height)
print("Стороны:", side1, ",", side2, ",", side3)
print("Площадь:", triangle_area)
print("Периметр:", triangle_perimeter)