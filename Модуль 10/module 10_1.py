from time import sleep
from threading import Thread
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        # Записываем слова
        for i in range(word_count):
            file.write(f'Какое-то слово № {i+1}\n')
            sleep(0.1)  # Пауза после каждой записи
    print(f'Завершилась запись в файл {file_name}')

# Замер времени
start_time = datetime.now()

# Последовательный вызов функций
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Вычисление времени работы функций
function_time = datetime.now() - start_time
print(f'Работа функций {function_time}')

# Замер времени для параллельного выполнения в потоках
thread_start_time = datetime.now()

threads = [
    Thread(target=write_words, args=(10, 'example5.txt')),
    Thread(target=write_words, args=(30, 'example6.txt')),
    Thread(target=write_words, args=(200, 'example7.txt')),
    Thread(target=write_words, args=(100, 'example8.txt'))
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

thread_time = datetime.now() - thread_start_time
print(f'Работа потоков {thread_time}')