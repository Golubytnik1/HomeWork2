#04.11.2022
# bool - boolean (логический тип данных)
# True, False
# or, and, not - логические операторы
# in, is
# [start:stop:step]

# shoes_black = '34-38'
# first = int(shoes_black[:2])
# second = int(shoes_black[3:])
# print((second-first) // 2 + 1)

#word = 'стоматолог'
#cut = word[4:]
#print(word)
#print(cut)
#print(word[1:6:])
#print(word[[start:stop:step])


# print(word[0])
# print(word[3])
# print(word[-1])


# print(word.endswith('n'))
# print(word.startswith('n'))
# print('o' in word)
# print(word.count('o'))

# print(type(True))
# print(2 != 2)
# print(2 == 3-1)
# print(4 > 7)
# print(4 < 8)
# print(2 >= 1)
# print(2 > 1 or 2 == 1)
# print(2 > 1 and 4 < 2) - укороченная запись (a <> b)
# print(1 < 2 > 4) - полная запись (a <> b)

# оператор назначения
# a = 5
# a = a + 2
# a += 2
#print(a)

# time = input('укажите время: ')
# # time = 'Чуй'
#
# if time == 'morning' or time == "утро":
#     print('good morning')
# elif time == 'day' or time == "день":
#     print('good afternoon')
# elif time == 'evening' or time == "вечер":
#     print('good evening')
# else:
#     print('hello')

# password = 'dada1122'

# input_password = input('введите пароль: ')
# if input_password == password:
#     print("С возвращением дорогой пользователь!")
# else:
#     print("Вы забыли пароль?")


attempts = int(input('сколько попыток? '))

for i in range(1, attempts+1):
    password = input('enter password: ')

    if len(password) >= 6 and not password.isdigit() and not password.isalpha():
        print('ok')
    else:
        print(f'no, your password lenght is {len(password)}\n'
              f'пароль должен состоять из числ и букв, а также длиннее 5')

#print(len(password))
#print(password.isdigit())
#print(password.isalpha())



