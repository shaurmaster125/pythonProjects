first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

#сборка с использованием zip
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

#сборка с использованием range и len
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))