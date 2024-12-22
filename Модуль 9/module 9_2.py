first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Первый результат: длины строк не менее 5 символов
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Второй результат: пары слов одинаковой длины
second_result = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]

# Третий результат: словарь строка-длина для строк четной длины
third_result = {s: len(s) for s in (first_strings + second_strings) if len(s) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)