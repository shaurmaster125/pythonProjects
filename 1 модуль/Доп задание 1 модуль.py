# Данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Создаем пустой словарь для хранения среднего балла
average_grades = {}

# Преобразуем множество в отсортированный список
sorted_students = list(sorted(students))

# Обходим каждого студента и соответствующие оценки
for student, grade in zip(sorted_students, grades):
    # Вычисляем средний балл
    avg_grade = sum(grade) / len(grade)
    # Заполняем словарь
    average_grades[student] = avg_grade

# Выводим результат
print(average_grades)