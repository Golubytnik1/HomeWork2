#15.11.2022 - dz4.1`

mentors = ["Аблай", "Камиля", "Марлен"]

while True:
    user_input = int(input('Команды: Добавление[1], Изменение[2], Удаление[3], Выход[0]: '))

# Добавление
    if user_input == 1:
        new_mentor = input('Введите имя: ').title()
        if not new_mentor.isalpha():
            print('Принимаются только буквы!')
        else:
            if len(mentors) == 5:
                print('Привышено максимальное количество менторов - 5')
            else:
                if len(new_mentor) <= 15:
                    mentors.append(new_mentor)
                    if mentors.count(new_mentor) != 1:
                        print('Ментор уже в списке!')
                        mentors.remove(new_mentor)
                else:
                    print('Имя должно содержать не более 15 символов!')

# Изменение
    if user_input == 2:
        print('Кого вы хотите заменить?')
        edit_mentor = input(f'Ваш список менторов: {mentors} \nВведите старое имя: ')
        for i in mentors:
            if edit_mentor in mentors:
                imentors = mentors.index(edit_mentor)
                new_mentors = input('Введите новое имя: ').title()
                if not new_mentors.isalpha():
                    print('Принимаются только буквы!')
                else:
                    if len(new_mentors) <= 15:
                        if new_mentors not in mentors:
                            mentors[imentors] = new_mentors
                        else:
                            print('Ваш ментор уже в списке')
                    else:
                        print('Имя должно содержать не более 15 символов!')

# Удаление
    if user_input == 3:
        print(f'Ваш актуальный список: {mentors} \n Режим: удалить по индексу[1], удалить по имени[2]: ')
        del_input = int(input('Режим: '))
        if del_input == 1:
            imentors_input = int(input('Введите индекс удаляемого ментора: '))
            m = len(mentors)
            if m < imentors_input:
                print('Введен не существующий индекс')
            else:
                del mentors[imentors_input]
                print('Ваш ментор успешно удален!')
        if del_input == 2:
            name_input = input('Введите имя: ').title()
            if name_input in mentors:
                mentors.remove(name_input)
            else:
                print('Убедитесь в правильности введенных данных!')

# Выход
    if user_input == 0:
        print('До скорого!')
        break

mentors = tuple(mentors)
print('Актуальный список менторов:', mentors)