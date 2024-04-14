import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def calculate_circle_area(radius):
        Circle.calculate_circle_perimeter(radius)
        return print('Площадь окружности равен: ',math.pi * radius ** 2)

    @staticmethod
    def calculate_circle_perimeter(radius):
        return print('Периметр окружности равен: ',2 * math.pi * radius)

Circle.calculate_circle_area(3)