# 15.11.2022
# словари, множества
# dict - dictionary (словарь)
# set - множество
# {key: value}

"""функция dict"""
# new = dict(([1, 'one'], [2, 'two']))
# new = dict(enumerate('oop'))
# other_student = dict(name='Amir', age=16, country='kgz')
# print(new)

student = {
    'name': 'Maulen',
    'age': 20,
    'weight': 70.6,
    'born_place': ('bishkek', 'kgz'),
    'hobby': ['gitarre spielen', 'tanzen']
}

# numbers = {n: n**2 for n in range(1, 4)}
# print(numbers)

for i in student.items():
    print(i)

for k, v in student.items():
    print(k, '==>', v)

for i in student:
    print(f'{i}: {student[i]}')

# print(student.keys())
# print(student.values())
# print(student.items())

"""add(добавление)"""
# student['favorite food'] = ['plov', 'manti']
# student.update(other_student)
# print(student)

"""edit(изменение)"""
# student['weight'] += 3.4
# student['hobby'] = tuple(student['hobby'])
# student['hobby'][1] = student['hobby'][1],
# print(student)

"""delete(удаление)"""
# deleted = student.pop('born_place')
# print(deleted)
# del student['hobby'][1]

# print(student.get('age', 'нет такого ключа!')) - при неправильном введение ключа выйдет альтернатива
# print(student['ag']) - KeyError

"""множества"""
# numbers = [1, 2, 3, 2, 3, 4, 'a', 'a']
# numbers1 = {1, 2, 3, 2, 3, 4, 'a', 'a'}
#
# print(numbers)
# print(numbers1)
# print(type(numbers1))

# drug = {'меф', 'героин', 'спайс', 'меланхолин'}
# cig = {'мальборро', 'вест', 'кастер', 'меланхолин'}

# print(drug - cig)
# print(drug.difference(cig))

# print(drug.union(cig))
# print(drug | cig)

# print(drug.intersection(cig))
# print(drug & cig)

# print(drug.symmetric_difference(cig))
# print(drug ^ cig)

"""доп. задание
создать возможность поиска блюда по нескольким ингридиентам
"""

menu = {
    'ramen': {'noodles', 'egg', 'pepper'},
    'beshbarmak': {'noodles', 'onion', 'meat'}
}

while True:
    user_input = input('введите продукт: ')
    if user_input in menu.keys():
        print(menu[user_input])

    for name, ingrs in menu.items():
        if user_input in ingrs:
            print(name)
        else:
            break
