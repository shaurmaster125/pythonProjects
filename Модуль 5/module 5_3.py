class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.floors}"

    # Операторы сравнения
    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors != other.floors
        return True

    # Арифметические операторы
    def __add__(self, value):
        if isinstance(value, int):
            self.floors += value
            return self
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


# Тестирование
if __name__ == "__main__":
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)

    print(h1)
    print(h2)
    print(h1 == h2)

    h1 = h1 + 10
    print(h1)
    print(h1 == h2)

    h1 += 10
    print(h1)

    h2 = 10 + h2
    print(h2)

    print(h1 > h2)
    print(h1 >= h2)
    print(h1 < h2)
    print(h1 <= h2)
    print(h1 != h2)