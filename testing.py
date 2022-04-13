# s = lambda a, b: a + b
# print(s(2, 4))
# list = [5, 3, 0, -6, 8, 10, 1]
# def get_filter(a, filter=None):
#     if filter is None:
#         return a
#     res = []
#     for x in a:
#         if filter(x):
#             res.append(x)
#     return res


# r = get_filter(list, lambda x: x % 2== 0)
# print(r)
# print(sorted([(1, 'value'),(2, 'end')], key=lambda x: x[1]))

# class Shop:
#
#     all_products = []
#     all_prices = []
#
#     def __init__(self, title):
#         self.title = title
#         self._price = 0
#         self.all_products.append(self)
#
#     @property
#     def price(self):
#         return self._price
#
#     @price.setter
#     def price(self, value):
#         self._price = value
#         self.all_prices.append(value)
#
#     @classmethod
#     def sum_overall_price(cls):
#         overall_price = sum(cls.all_prices)
#         return overall_price
#
#
# google_pixel_5 = Shop('Google Pixel 5')
# google_pixel_5.price = 500
#
# google_pixel_6 = Shop('Google Pixel 6')
# google_pixel_6.price = 1000
#
# google_pixel_7 = Shop('Google Pixel 7')
# google_pixel_7.price = 250
#
# # google_pixel_5 = Shop('Google Pixel 5')
# google_pixel_5.price = 123
# print(Shop.sum_overall_price())


# class BankAccount:
#     def __init__(self,name, balance, passport):
#         self.__name = name
#         self.__balance = balance
#         self.__passport = passport
#
#     # def print_public_data(self):
#     #     print(self.name, self.balance, self.passport)
#
#     # def print_protected_data(self):
#     #     print(self._name, self._balance, self._passport)
#
#     def __print_private_data(self):
#         print(self.__name, self.__balance, self.__passport)
#
# ac1 = BankAccount('Bob', 100000, 4233642)
# # ac1.print_protected_data()
# ac1.print__private_data()
# print(ac1.__name)
# print(ac1.__balance)
# print(ac1.__passport)
import random
class Units:
    def __init__(self, id, team):
        self.id = id
        self.team = team

class Hero(Units):
    def __init__(self, id, team, lvl):
        Units.__init__(self, id, team)
        self.lvl = lvl

    def level_up(self):
        self.lvl += 1
        print(f'Уровень героя №{self.id} увеличен на 1 и равен {self.lvl}')

class Solder(Units):
    def move_to_hero(self, Hero):
        print(f"Солдат №{self.id} следует за героем {Hero.id}")
def add_solders():
    for elt in range(17):
        numb = random.randint(1,2)
        if numb == 1:
            team_hero_1.append(Solder(elt, 'red'))
        else:
            team_hero_2.append(Solder(elt, 'blue'))

def up_level():
    if len(team_hero_1) > len(team_hero_2):
        Hero.level_up(h1)
    else:
        Hero.level_up(h2)
h1 = Hero(1, 'red', 1)
h2 = Hero(2, 'blue', 1)
team_hero_1 = []
team_hero_2 = []
add_solders()
up_level()
add_solders()
up_level()
random.choice(team_hero_1).move_to_hero(h1)
random.choice(team_hero_2).move_to_hero(h2)







# class Soldiers():
#     id_ = 1
#
#     def __init__(self):
#         self.id_ = Soldiers.id_
#         Soldiers.id_ += 1
#
#     def go_hero(self, hero):
#         print(f'солдат с id {self.id_} следует за героем {hero.id_}')
#
#     def __str__(self):
#         return f'{self.id_}'
#
#
# class Heroes(Soldiers):
#
#     def __init__(self, team):
#         Soldiers.__init__(self)
#         self.team = team
#         self.level = 0
#
#     def level_up(self):
#         self.level += 1
#         print(f'герой с id {self.id_} достиг {self.level} уровня')
#
#
# heroes = Heroes('red')
# heroes_2 = Heroes('blue')
# list_heroes = []
# list_heroes_2 = []
# for _ in range(50):
#     if random.choice(['red', 'blue']) == 'red':
#         list_heroes.append(Soldiers())
#     else:
#         list_heroes_2.append(Soldiers())

# len_heroes = len(list_heroes)
# len_heroes_2 = len(list_heroes_2)
# print(f'солдат у героя heroes - {len_heroes}')
# print(f'солдат у героя heroes_2 - {len_heroes_2}')
# if len_heroes > len_heroes_2:
#     heroes.level_up()
# else:
#     heroes_2.level_up()
#
# random.choice(list_heroes).go_hero(heroes)



# import random
#
#
# class Unit:
#     def __init__(self, number, commandid):
#         self.number = number
#         self.commandId = commandid
#
#
# class Hero(Unit):
#     def __init__(self,  number, commandid, name, level=1):  # При инициализации добавляем свойства name и level
#         Unit.__init__(self, number, commandid)
#         self.name = name  # Привязываем классу Hero свойство level и name
#         self.level = level
#
#     def getlevel(self):
#         return self.level
#
#     def inclevel(self):
#         self.level += 1
#         print('Уровень героя', self.name,'увеличен на 1 и равен', self.level)
#
#
# class Soldier(Unit):
#     def gotohero(self, Hero):
#         print('Солдат номер', self.number, 'следует за героем', Hero.name, 'с номером', Hero.number)
#
#
# H1 = Hero(1, 1, 'Arthas')  # Создаем героев с номерами 1 и 2
# H2 = Hero(2, 2, 'Illidan')
# armyH1, armyH2 = [], []  # Списки солдат
#
# for i in range(3, 10):  # Генерим нечетное количество солдат
#     n = random.randint(0, 1)
#     if n:
#         armyH1.append(Soldier(i, 1))
#         print('Солдат с номером', i, 'добавлен в армию', H1.name)
#     else:
#         armyH2.append(Soldier(i, 2))
#         print('Солдат с номером', i, 'добавлен в армию', H2.name)
#
# print('Армия героя', H1.name, ':', len(armyH1))
# print('Армия героя', H2.name, ':', len(armyH2))
#
# if len(armyH1) > len(armyH2):
#     print('В армии', H1.name, 'больше солдат, увеличиваем его уровень')
#     H1.inclevel()
# else:
#     print('В армии', H2.name, 'больше солдат, увеличиваем его уровень')
#     H2.inclevel()
#
# armyH1[1].gotohero(H2)

