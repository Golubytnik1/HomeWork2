#str - string (строка)
#int - integer (целое)
#float - floating (дробное)
#upper
#lower
#title
#input

# name = input('укажите имя: ').lower()
# surname = input('укажите фамилие: ').title()
# age = int(input('укажите возраст: '))

# print(f'Приветствуем вас {name} {surname}')

# print('Hello {} {}'.format(name, surname))

# print('Hello', name, surname)
# print(int(16 + age))

# a = 6
# b = 2
# print(b + a)

# c = round(a / b, 3)
#print((a + b) * 3)
#print(a + b * 3)
#print(a + b)
#print(a - b)
#print(a * b)
# print(a // b)

sum_ages = 17 + 36 + 18 + 16 + 15 + 18 + 17 + 15 + 16 + 22 + 33 + 17
amount_students = 23
average_age = sum_ages / amount_students
print(round(average_age, 2))
print('%2f' % average_age)
