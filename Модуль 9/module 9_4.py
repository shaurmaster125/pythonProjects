from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

compare = lambda x, y: x.lower() == y.lower()
result = list(map(compare, first, second))

# Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            for item in data_set:
                file.write(str(item) + '\n')

    return write_everything


#использование замыкания
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Класс с методом __call__
class MysticBall:
    def __init__(self, *words):
        self.words = list(words)

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())  # Случайное слово
print(first_ball())  # Случайное слово
print(first_ball())  # Случайное слово