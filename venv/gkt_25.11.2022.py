# 25.11.2022
# работа с файлами txt
# w - write
# r - read
# a - add
# x - safety method

# new = open('file.txt', 'w', encoding='UTF-8')
# new.write('Чемпионат Мира 2022')
# new.close()

# with open('new.txt', 'w') as file: # w - перезапись чего-либо в файле
#     file.write('Amirrr')

# with open('new.txt', 'a') as file: # a - добавить что-то к сущ. записи
#     file.write('\n2222222222')
#
# with open('new.txt', 'x') as file:
#     file.write('asfasfsdgsdgdsgds')

# from time import sleep as spat

# with open('new.txt', 'r', encoding='UTF-8') as file:
#     for letter in file.readlines():
#         sleep(1)
#         print(letter, end='')
    # print(file.read())
    # print(file.readlines()[2].split()[0])
    # print(file.readline())

# while True:
#     filename = input('введите название: ')
#     if filename == 'exit':
#         break
#     with open(f'{filename}.txt', 'w') as file:
#         file.write(input('Что хотели бы записать? \n'))

left = 1
right = 100
while True:
    current = (left+right)//2
    is_right = input('Ваше число:{}?(да, больше, меньше)'.format(current))
    if is_right.lower() == 'да':
        print('Я его угадал!')
        # continue
    elif is_right=='больше':
        left = current + 1
    else:
        right = current - 1
