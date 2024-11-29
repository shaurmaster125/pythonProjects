class Vehicle:
    # Атрибут класса - список допустимых цветов
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner  # Открытый атрибут - может меняться
        self.__model = model  # Скрытый атрибут - не может меняться
        self.__engine_power = engine_power  # Скрытый атрибут - не может меняться
        self.__color = color  # Скрытый атрибут - меняется только через метод

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        # Проверяем, есть ли новый цвет в списке допустимых (игнорируя регистр)
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    # Атрибут класса - ограничение по количеству пассажиров
    __PASSENGERS_LIMIT = 5

    # Наследуем все методы от класса Vehicle
    pass


# Тестирование
if __name__ == "__main__":
    #объект класса Sedan
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Проверяем начальные свойства
    vehicle1.print_info()
    print()

    # Пробуем изменить свойства
    vehicle1.set_color('Pink')  # Недопустимый цвет
    vehicle1.set_color('BLACK')  # Допустимый цвет
    vehicle1.owner = 'Vasyok'  # Меняем владельца

    # Проверяем изменения
    vehicle1.print_info()