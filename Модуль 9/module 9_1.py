def apply_all_func(int_list, *functions):
    results = {}

    for func in functions:
        # Применяем функцию к списку и сохраняем результат в словарь
        # используя имя функции как ключ
        results[func.__name__] = func(int_list)

    return results


# Примеры использования:
# Тест 1: с функциями max и min
print(apply_all_func([6, 20, 15, 9], max, min))

# Тест 2: с функциями len, sum и sorted
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))