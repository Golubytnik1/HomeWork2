#dz - 20.11.2022

#1
def func(word='Hello world'):
    if type(word) != str:
        return False
    else:
        return word.split()[0]

print(func())


#2
def numbers(a, *args):
    return sum(args) / a
print(int(numbers(10, 2, 34, 12, 6, 28, 16, 21, 9, 3, 6)))


# #3
def user_password(password):
    if len(password) >= 6:
        return True
    else:
        return False
        isalpha = False
        isdigits = False
        for p in password:
            if p.isalpha():
                isalpha = True
            elif p.isdigits:
                isdigits = True
                return isalpha and isdigits
            else:
                return False

print(user_password('ptizoed1122'))