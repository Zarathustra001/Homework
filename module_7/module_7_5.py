#Пример входных данных
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# Использование оператора % для форматирования строк

# Сценарий 1: Количество участников первой команды
result_1 = "В команде Мастера кода участников: %d !" % team1_num
print(result_1)

# Сценарий 2: Количество участников в обеих командах
result_2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(result_2)

# Использование метода str.format()

# Сценарий 3: Количество задач, решённых командой 2
result_3 = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(result_3)

# Сценарий 4: Время, за которое команда 2 решила задачи
result_4 = "Волшебники данных решили задачи за {:.1f} с !".format(team2_time)
print(result_4)

# Использование f-строк (f-strings)

# Сценарий 5: Количество решённых задач по командам
result_5 = f"Команды решили {score_1} и {score_2} задач."
print(result_5)

# Сценарий 6: Исход соревнования
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    team_1win = f"Результат битвы: Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    team2_win = f"Результат битвы: Победа команды Волшебники Данных!"
else:
    result = 'Ничья!'

# Сценарий 7: Общее количество решённых задач и среднее время решения
result_7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!"
print(result_7)