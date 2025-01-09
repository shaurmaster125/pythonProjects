from threading import Thread
import time


class Knight(Thread):
    enemies = 100  # общее количество врагов для всех рыцарей

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        days = 0

        while Knight.enemies > 0:
            days += 1
            time.sleep(1)  # задержка в 1 секунду (1 день)

            # уменьшаем количество врагов на величину силы рыцаря
            if Knight.enemies >= self.power:
                Knight.enemies -= self.power
            else:
                Knight.enemies = 0

            print(f"{self.name} сражается {days} день(дня)..., осталось {Knight.enemies} воинов.")

            if Knight.enemies <= 0:
                print(f"{self.name} одержал победу спустя {days} дней(дня)!")
                break

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения обоих потоков
first_knight.join()
second_knight.join()

print("Все битвы закончились!")