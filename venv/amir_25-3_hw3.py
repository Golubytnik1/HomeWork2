#dz - 08.11.2022

print('Для выхода из программы введите "exit" или "выход"')

while True:
    user_input = input('введите слово: ').lower()
    amount = len(user_input)
    consonants = 0
    vowels = 0

    if user_input == 'exit':
        break
    if user_input == 'выход':
        break

    for i in user_input:
        if i in ('цкнгшщзхфвпрлджчсмтбbcdfghjklmnpqrstvwxyz'):
            consonants += 1
        elif i in ('йуеыаоэяиюaeiouy'):
            vowels += 1
        else:
            break
    per_con = round((consonants / amount) * 100, 2)
    per_vow = round((vowels / amount) * 100, 2)

    if i in "1234567890":
        print('Убедитесь в правильности введенных данных!')
    else:
        print(f'Слово: {user_input}')
        print(f'Количество букв: {amount}')
        print(f'Количество согласных букв: {consonants}')
        print(f'Количество гласных букв: {vowels}')
        print(f'Гласные/Согласные: {per_con}%/{per_vow}%')
