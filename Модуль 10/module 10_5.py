from multiprocessing import Pool
from datetime import datetime
import time

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()

if __name__ == '__main__':
    # Создаем список имен файлов
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = datetime.now()
    for filename in filenames:
        read_info(filename)
    end_time = datetime.now()
    print(f"Линейное выполнение: {end_time - start_time}")

    # Многопроцессный вызов
    start_time = datetime.now()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = datetime.now()
    print(f"Многопроцессное выполнение: {end_time - start_time}")