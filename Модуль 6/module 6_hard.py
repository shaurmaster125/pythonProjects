import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]
        self.filled = True
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        return all(isinstance(x, (int, float)) and x > 0 for x in sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        # Формула Герона
        a, b, c = self.get_sides()
        p = (a + b + c) / 2  # полупериметр
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            super().__init__(color, *[sides[0]] * self.sides_count)
        else:
            super().__init__(color, *sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


# Тестирование
if __name__ == "__main__":
    # Тесты из условия
    circle1 = Circle((200, 200, 100), 10)
    cube1 = Cube((222, 35, 130), 6)

    circle1.set_color(55, 66, 77)
    print(circle1.get_color())

    cube1.set_color(300, 70, 15)
    print(cube1.get_color())

    cube1.set_sides(5, 3, 12, 4, 5)
    print(cube1.get_sides())

    circle1.set_sides(15)
    print(circle1.get_sides())

    print(len(circle1))
    print(cube1.get_volume())

    # Дополнительные тесты
    print("\nДополнительные проверки:")

    triangle1 = Triangle((100, 100, 100), 3, 4, 5)
    print(f"Площадь треугольника: {triangle1.get_square()}")

    print(f"Площадь круга: {circle1.get_square()}")

    # Проверка некорректных значений
    circle2 = Circle((256, -1, 300), -5)  # Должны установиться значения по умолч
    print(f"Цвет circle2: {circle2.get_color()}")  # Должен быть [0, 0, 0]
    print(f"Стороны circle2: {circle2.get_sides()}")  # Должен быть [1]

    # Проверка изменения сторон куба
    cube2 = Cube((100, 100, 100), 2)
    print(f"\nСтороны куба изначально: {cube2.get_sides()}")
    cube2.set_sides(*[3] * 12)  # Корректное изменение
    print(f"Стороны куба после корректного изменения: {cube2.get_sides()}")
    cube2.set_sides(*[4] * 11)  # Некорректное изменение (неверное количество)
    print(f"Стороны куба после некорректного изменения: {cube2.get_sides()}")

    # Проверка вычисления периметров
    triangle2 = Triangle((100, 100, 100), 5, 5, 5)
    print(f"\nПериметр треугольника: {len(triangle2)}")
    print(f"Периметр куба: {len(cube2)}")

    # Проверка установки цвета
    triangle2.set_color(100, 150, 200)  # Корректные значения
    print(f"\nЦвет треугольника после корректного изменения: {triangle2.get_color()}")
    triangle2.set_color(-1, 300, 100)  # Некорректные значения
    print(f"Цвет треугольника после некорректного изменения: {triangle2.get_color()}")