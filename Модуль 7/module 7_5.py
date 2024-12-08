import os
import time

# Указываем директорию для обхода (текущая директория)
directory = "."

# Обходим все файлы в указанной директории и её поддиректориях
for root, dirs, files in os.walk(directory):
    for file in files:
        # Формируем полный путь к файлу
        filepath = os.path.join(root, file)

        # Получаем время последнего изменения файла
        filetime = os.path.getmtime(filepath)

        # Форматируем время в удобочитаемый вид
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Получаем размер файла в байтах
        filesize = os.path.getsize(filepath)

        # Получаем родительскую директорию
        parent_dir = os.path.dirname(filepath)

        # Выводим информацию о файле
        print(f'Обнаружен файл: {file}')
        print(f'Путь: {filepath}')
        print(f'Размер: {filesize} байт')
        print(f'Время изменения: {formatted_time}')
        print(f'Родительская директория: {parent_dir}')
        print('-' * 50)  # Разделитель для удобства чтения