#08.11.2022
#for, while - циклы
#item, iterable

# cash = 100
# percent = 0.1
# years = 5
# counter = 1

# for year in range(1, years+1):
#     cash = round(cash * percent + cash, 1)
#     print(f'year: {counter} - {cash}')
#     counter += 1


# c = 0
# while c != 5:
#     c += 1# while True:
# #     print('hello', c)
# #     c += 1
# #     if c == 1000:
# #         break
#
#
# # for i in range(1, 4):
# #     for k in range(1, 4):
# #         print(i, k)
#
#
# # word = 'аксессуар'
# #
# # for letter in word:
# #     if letter == 'с':
# #         print("мы пропускаем 'с'")
# #         continue
# #     print(letter)
#     if c == 3:
#         print('мы устали')
#         continue
#     print(c)


# c = 0


    #     print('цикл завершен!')
    #     break
    # print(letter)
    # print(letter, end='')


# print(len(eng) == len(rus))
eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,. "
rus = "йцукенгшщзхъфывапролджэячсмитьбю "

while True:
    user_input = input('\nвведите слово: ').lower()
    if user_input == 'exit':
        break
    for i in user_input:
        if i in eng:
            print(rus[eng.index(i)], end='')
        elif i in rus:
            print(eng[rus.index(i)], end='')
        else:
            print('введите значение на англ или русс раскладке!')

# print(rus[eng.index('r')])