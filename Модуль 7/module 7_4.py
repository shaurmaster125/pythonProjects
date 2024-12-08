# Входные данные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# Использование %
# Вариант 1
print("В команде Мастера кода участников: %d !" % team1_num)

# Вариант 2
print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))

# Использование format()
# Вариант 1
print("Команда Волшебники данных решила задач: {} !".format(score_2))

# Вариант 2
print("Волшебники данных решили задачи за {:.1f} с !".format(team2_time))

# Использование f-строк
# Вариант 1
print(f"Команды решили {score_1} и {score_2} задач.")

# Вариант 2
print(f"Результат битвы: {challenge_result}")

# Вариант 3
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")

# Дополнительно: расчёт challenge_result
if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    result = 'Победа команды Волшебники данных!'
else:
    result = 'Ничья!'

print(f"Результат соревнования: {result}")