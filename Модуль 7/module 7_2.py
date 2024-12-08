def custom_write(file_name, strings):
    # Создаем пустой словарь для хранения позиций строк
    strings_positions = {}

    # Открываем файл для записи в кодировке utf-8
    with open(file_name, 'w', encoding='utf-8') as file:
        # Перебираем строки из списка с их номерами (начиная с 1)
        for line_number, line in enumerate(strings, 1):
            # Получаем текущую позицию в файле
            position = file.tell()
            # Записываем строку с переносом строки
            file.write(line + '\n')
            # Добавляем в словарь кортеж (номер строки, позиция) и саму строку
            strings_positions[(line_number, position)] = line

    return strings_positions


# Пример использования
if __name__ == "__main__":
    # Тестовый список строк
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    # Вызываем функцию и получаем результат
    result = custom_write('test.txt', info)

    # Выводим результат
    for elem in result.items():
        print(elem)