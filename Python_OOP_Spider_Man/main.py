class Man:

    def __init__(self, name, power, energy=100, hands=2): #all those attributes will be common for all instances
        self.name = name #we can change those attributes for each instance
        self.power = power
        self.energy = energy
        self.hands = hands

    def move(self):
        print('Moving on 2 squares')

    def eat(self, food):
        if self.energy < 100:
            self.energy += food
        else:
            print('Not hungry')

    def attack(self, enemy):
        enemy.health -= 10

    def do_exercise(self, hours):
        if self.energy > 0:
            self.energy -= hours * 2
            self.power += hours * 2
        else:
            print('Too tired')

    def change_alias(self, new_alias):
        print(self)
        self.alias = new_alias

    def beat_up(self, enemy):
        if not isinstance(enemy, Character): #checking if enemy belongs to Class Character
            return
        if enemy.power < self.power:
            enemy.status = 'defeated'
            self.status = 'winner'
        else:
            print('Retreat!')


class Spider:

    def __init__(self, power, energy=50, hands=8):
        self.power = power
        self.energy = energy
        self.hands = hands

    def webshoot(self):
        print('Pew_pew')

    def move(self):
        self.webshoot()
        print('Moving on 1 square')

    def attack(self, enemy):
        enemy.status = 'stunned'


class SpiderMan(Man, Spider):
    # we inherit everything from parent class and adding new attribute for an Instance with super()
    def __init__(self, name, power):
        super().__init__(name, power)
        self.backpack = []

    def turn_spider_sence(self):
        self.energy -= 10
        self.power += 20

    def move(self):
        self.webshoot()
        print('Moving on 3 squares')

    def webshoot(self):
        if 'web' in self.backpack:
            super().webshoot() #with super() we will take a webshoot from parent class Spider
        else:
            print('No web')

    def attack(self, enemy):
        super().attack(enemy) #call attack() from Character, because of mro
        Spider.attack(self, enemy) #call attack() from Spider directly from the class Spider

    def __lt__(self, other):
        if not isinstance(other, Man):
            print('Not a Character')
            return
        return self.power < other.power

    def __str__(self):
        res = f"Character's power = {self.power}"
        return res

peter_parker = SpiderMan('Peter Parker', 80)
miles_morales = SpiderMan('Miles Morales', 85)

print(peter_parker < miles_morales)
print(peter_parker)


enemy = Man('Some enemy', 10)
enemy.health = 100

peter_parker.attack(enemy)

print(enemy.health)
print(enemy.status)




