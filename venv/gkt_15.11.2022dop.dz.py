menu = {
    'ramen': {'noodles', 'egg', 'pepper'},
    'beshbarmak': {'noodles', 'onion', 'meat'},
    'lagman': {'egg', 'oil', 'flour'},
    'plov': {'rice', 'carrot', 'meat', 'egg'},
    'manti': {'dough', 'meat', 'cartoffel'},
    'pelmeni': {'dough', 'meat', 'onion'},
    'ash-lyamfu': {'starch', 'ginger', 'salt', 'star anise'},
    'olivie': {'carrot', 'egg', 'sausage', 'cartoffel', 'cucumber'},
}

while True:
    user_input = input('Введите ингридиент блюда: ').split(' ')
    ex = 0
    for name, ingrs in menu.items():
        sum = 0
        for k in user_input:
            if k in ingrs:
                sum += 1
            if sum == len(user_input):
                print(name)
                ex += 1
    if ex == 0:
        print("Такое блюдо отсутсвует с данным ингридиентом!")