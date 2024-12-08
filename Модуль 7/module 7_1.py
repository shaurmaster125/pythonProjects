class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        # Получаем текущие продукты
        current_products = self.get_products()

        # Открываем файл для добавления
        with open(self.__file_name, 'a') as file:
            for product in products:
                # Проверяем, есть ли продукт уже в файле
                if product.name in current_products:
                    print(f"Продукт {product.name} уже есть в магазине")
                else:
                    # Добавляем новый продукт
                    file.write(f"{product}\n")


# Пример использования:
if __name__ == "__main__":
    s1 = Shop()

    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # Выводит: Spaghetti, 3.4, Groceries

    s1.add(p1, p2, p3)

    print(s1.get_products())