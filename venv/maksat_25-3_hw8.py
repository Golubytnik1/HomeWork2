import random
print('Загадайте число от 1 до 100, а компьютер угадает его!')

count = 0
min = 1
max  = 100
list = []
correct = []

while True:
    game = (min + max)// 2
    user_input = input(f'Ваше число - {game}? да, больше или меньше: ').lower()
    if user_input == 'да':
        list.append(game)
        correct.append(game)
        count += 1
        print('Ура, моя взяла!')
        with open('results.txt', 'w', encoding='UTF-8') as file:
            file.write(f'Кол-во попыток: {count}; \nСписок попыток: {list}; \nЗагаданное число: {correct}')
        break
    elif user_input == 'больше':
        min = game + 1
        list.append(game)
        count += 1
    elif user_input == 'меньше':
        max = game - 1
        list.append(game)
        count += 1
    else:
        print("Введите пожайлуста правильно: да, больше или меньше!")

