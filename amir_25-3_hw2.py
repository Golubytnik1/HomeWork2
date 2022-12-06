#dz

date1 = int(input("Введите день рождения: "))
date2 = int(input("Введите месяц рождения: "))

if (date1 >= 22 and date1 <= 31 and date2 == 12) or (date1 >= 1 and date1 <= 20 and date2 == 1):
    print('Козерог')

elif (date1 >= 21 and date1 <= 31 and date2 == 1) or (date1 >= 1 and date1 <= 18 and date2 == 2):
    print('Водолей')

elif (date1 >= 19 and date1 <= 29 and date2 == 2) or (date1 >= 1 and date1 <= 20 and date2 == 3):
    print('Рыбы')

elif (date1 >= 21 and date1 <= 31 and date2 == 3) or (date1 >= 1 and date1 <= 19 and date2 == 4):
    print('Овен')

elif (date1 >= 20 and date1 <= 30 and date2 == 4) or (date1 >= 1 and date1 <= 20 and date2 == 5):
    print('Телец')

elif (date1 >= 21 and date1 <= 31 and date2 == 5) or (date1 >= 1 and date1 <= 21 and date2 == 6):
    print('Близнецы')

elif (date1 >= 22 and date1 <= 30 and date2 == 6) or (date1 >= 1 and date1 <= 22 and date2 == 7):
    print('Рак')

elif (date1 >= 23 and date1 <= 31 and date2 == 7) or (date1 >= 1 and date1 <= 22 and date2 == 8):
    print('Лев')

elif (date1 >= 23 and date1 <= 31 and date2 == 8) or (date1 >= 1 and date1 <= 22 and date2 == 9):
    print('Дева')

elif (date1 >= 23 and date1 <= 30 and date2 == 9) or (date1 >= 1 and date1 <= 23 and date2 == 10):
    print('Весы')

elif (date1 >= 24 and date1 <= 31 and date2 == 10) or (date1 >= 1 and date1 <= 22 and date2 == 11):
    print('Скорпион')

elif (date1 >= 23 and date1 <= 30 and date2 == 11) or (date1 >= 1 and date1 <= 21 and date2 == 12):
    print('Стрелец')
else:
    print('Вы точно уверены в правильности даты рождения?')
