class House:
    # Атрибут класса для хранения истории домов
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # Добавляем название дома в историю
        cls.houses_history.append(args[0])
        # Создаем и возвращаем новый экземпляр класса
        return super().__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __str__(self):
        return f"Дом {self.name} имеет {self.floors} этажей"

    def __eq__(self, other):
        return self.floors == other.floors

    def __lt__(self, other):
        return self.floors < other.floors

    def __le__(self, other):
        return self.floors <= other.floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


# Тестирование
if __name__ == "__main__":
    # Создаем объекты
    h1 = House('ЖК Эльбрус', 10)
    print(House.houses_history)

    h2 = House('ЖК Акация', 20)
    print(House.houses_history)

    h3 = House('ЖК Матрёшки', 20)
    print(House.houses_history)

    # Удаляем объекты
    del h2
    del h3

    print(House.houses_history)