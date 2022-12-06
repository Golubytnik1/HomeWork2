#dz - 24.11.2022

ten = list(range(1, 100))

evens = list(filter(lambda i: i % 2 == 0, ten))
evens_num2 = list(map(lambda i: i ** 2, evens))

print(evens_num2)

def func(list=ten):
    while True:
        print(ten)
        evensi = input("Введите индекс из списка: ").lower()
        if evensi == 'exit':
            print('Спасибо за внимание!')
            break
        try:
            print(list[int(evensi)])
        except IndexError:
            print('Введен неверный индекс; индекс начинается с 0 до 9')

func()
