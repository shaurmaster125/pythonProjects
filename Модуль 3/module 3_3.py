#функции с различными аргументами
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(25)
print_params(42, 'другая строка')
print_params(b=25)
print_params(c=[1, 2, 3])

#Распаковка + отдельные параметры
values_list = [3.141, 'текст', False]
values_dict = {
    'a': 100,
    'b': 'слово',
    'c': None
}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [122.32, 'Строка']
print_params(*values_list_2, 42)