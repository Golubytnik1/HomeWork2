#18.11.2022
# функции, аргументы: *args, **kwargs.
# DRY - don't repaet yourself
# def - definition


# def greet(name='name', surname='surname'):  #name - обязательный позиционный параметр
#     print(f'name: {name.title()}, surname: {surname.title()}')
# greet('dmitry', 'kluchevsky') #dmitry - обязательный позиционный аргумент
# greet(surname='koduranov', name='ilias') #keyword arguments (именованные аргументы)
# greet()
#
# def len1(sequence: str or list) -> int:
#     """Принимает последовательности, возвращает кол-во элементов
#     в указанной последовательности
#     """
#     word_count = 0
#     for i in sequence:
#         word_count += 1
#     return word_count
# print(len1('bishkek'))
# print(len1.__doc__)

# num = len('python')
# print(num + num)
# print(len('python'))

# width = 5
# lenght = 7
# square_2 = width * lenght
# print(square_2)

# width = 8
# lenght = 15
# square_hall = width * lenght
# print(square_hall)

""" Доп. задание
написать свои варианты функций sum(), max(), min()"""
# print(sum([1, 2, 3]))
# print(max([1, 2, 3]))
# print(min([1, 2, 3]))

def plus(a, *args):
    print(f'a: {a}, args: {args}')
    return sum(args) / a
print(plus(2, 4, 34, 12, 6))

# def days(**kwargs):
#     return sum(kwargs.value())
# print(days(monday=1, tuesday=2))


