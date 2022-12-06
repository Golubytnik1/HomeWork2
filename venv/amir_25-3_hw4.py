#13.11.2022

data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []

amir = list(data_tuple)
letters = [i for i in amir if type(i) == str]
numbers = [i for i in amir if type(i) != str]
numbers.remove(6.13)
numbers.remove(True)
letters.append(True)
numbers.insert(1, 2)
numbers.sort()
letters.reverse()
letters[1] = letters[1].title()
letters[-2] = letters[-2].lower()
numbers[0] *= 1
numbers[1] *= 2
numbers[2] *= 3

letters = tuple(letters)
numbers = tuple(numbers)

print(letters)
print(numbers)
