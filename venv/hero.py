# 07.12.2022

#(1)
class SuperHero:
    people = 'people'

    #(2)
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.health_points  = health_points
        self.nickname = nickname
        self.superpower = superpower
        self.catchphrase = catchphrase

    #(3)
    def n(self):
        print(f'Wanted: {self.name}')

    #(4)
    def h(self):
        hero.health = self.health_points * 2
        print(f'2XHP: {hero.health}')

    #(5)
    def __str__(self):
        return f'Nickname: {self.nickname}' \
               f'Power: {self.superpower}' \
               f'Health: {self.health_points}'

    #(6)
    def __len__(self):
        return len(self.catchphrase)

#(7)
hero = SuperHero('Monkey D. Luffy', 'Mugiwarra\n', 'Gomu Gomu\n', 70, 'GomuGomuNoPISTOLET')
hero.n()
hero.h()
print(hero)
print(f'Catchphrase: {len(hero.catchphrase)}')


