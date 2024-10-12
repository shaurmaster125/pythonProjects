#Словари
my_dict = {
    'Вася': 1975,
    'Олег': 1999,
    'Маша': 2002
}
print("Словарь:", my_dict)

existing_value = my_dict.get('Маша')
print("Существующее значение:", existing_value)
not_existing_value = my_dict.get('Андрей')
print("Несуществующее значение:", not_existing_value)

my_dict['Алиса'] = 1987
my_dict['Артем'] = 1985

deleted_value = my_dict.pop('Олег')
print("Удаленное значение:", deleted_value)

print("Новый словарь:", my_dict)

#Множества
my_set = {1, 'Яблоко', 42.314, 1, 'Яблоко', 3}

print("Множество:", my_set)

my_set.add(13)
my_set.add((5, 6, 1.6))

my_set.pop()

print("Новое множество:", my_set)