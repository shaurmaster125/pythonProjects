def is_prime(func):
    def wrapper(*args, **kwargs):
        # Получаем результат оригинальной функции
        result = func(*args, **kwargs)

        # Проверяем, является ли число простым
        if result < 2:
            print("Составное")
        else:
            is_prime = True
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    is_prime = False
                    break
            print("Простое" if is_prime else "Составное")

        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


# Пример использования
result = sum_three(2, 3, 6)
print(result)