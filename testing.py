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
# import random
# class Units:
#     def __init__(self, id, team):
#         self.id = id
#         self.team = team
#
# class Hero(Units):
#     def __init__(self, id, team, lvl):
#         Units.__init__(self, id, team)
#         self.lvl = lvl
#
#     def level_up(self):
#         self.lvl += 1
#         print(f'Уровень героя №{self.id} увеличен на 1 и равен {self.lvl}')
#
# class Solder(Units):
#     def move_to_hero(self, Hero):
#         print(f"Солдат №{self.id} следует за героем {Hero.id}")
# def add_solders():
#     for elt in range(17):
#         numb = random.randint(1,2)
#         if numb == 1:
#             team_hero_1.append(Solder(elt, 'red'))
#         else:
#             team_hero_2.append(Solder(elt, 'blue'))
#
# def up_level():
#     if len(team_hero_1) > len(team_hero_2):
#         Hero.level_up(h1)
#     else:
#         Hero.level_up(h2)
# h1 = Hero(1, 'red', 1)
# h2 = Hero(2, 'blue', 1)
# team_hero_1 = []
# team_hero_2 = []
# add_solders()
# up_level()
# add_solders()
# up_level()
# random.choice(team_hero_1).move_to_hero(h1)
# random.choice(team_hero_2).move_to_hero(h2)

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


# def solution(number):
#     total = []
#     for elt in range(1,number):
#         if (elt % 3 == 0) | (elt % 5 == 0):
#             total.append(elt)
#     print(sum(total))

# solution(10)


# word = "the quick brown fox jumps over the lazy dog"
# word_1 = 'Hello my director'
# def is_pangram(pangram):
# """def Pangram """
#     alphabet = "abcdefghiklmnopqrstuvwxyz"
#     pangram = pangram.lower()
#     empty = ''
#     for elt in alphabet:
#         if elt in pangram:
#             print(elt)
#             empty = empty + elt
#             print(empty)
#             continue
#     if alphabet == empty:
#         return True
#     else:
#         return False

# print(is_pangram(word))

# def duplicate_encode(word):
#     word_dup = word.lower()
#     check_list = []
#     empty = []
#     position = 0
#     for elt in word_dup.lower():
#         position += 1
#         if elt not in check_list and elt not in word_dup[position:]:
#             check_list.append(elt)
#             empty.append('(')
#             continue
#         else:
#             check_list.append(elt)
#             empty.append(')')
#             continue
#     empty = ''.join(empty)
#     print(empty)

# def dupp(word):
#     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

# a = 'hello world'
# b = 'recede'
# duplicate_encode(b)
# print(dupp(b))

# a = "This website is for losers LOLqqoOqIiIIIIi!"
# b = 'ieieiooeO'
# def disemvowel(xx):
#     x = list(xx)
#     q = 'ieieiooeOq'
#     qq = 'ieoqOI'
#     for elt in x[::]:
#         if elt in qq:
#             x.remove(elt)
#     x = ''.join(x)
#     return x
# print(disemvowel(a))

# def valid_braces(string):
#     parenthesis = []
#     pardict = {"{":"}", "[":"]", "(":")", "}":"{", "]":"[", ")":"("}
#     for i in range(len(string)):
#         if string[i] == "(" or string[i] == "[" or string[i] == "{":
#             parenthesis.append(string[i])
#         elif string[i].isalpha() == True:
#             continue
#         else:
#             if len(parenthesis) == 0:
#                 return False
#             elif pardict[string[i]] == parenthesis[len(parenthesis)-1]:
#                 del parenthesis[len(parenthesis)-1]
#             else:
#                 return False
#     if len(parenthesis) != 0:
#         return False
#     return True
# a = 'hi(hi)()'
# print(valid_braces(a))


# def fib(numb):
#     a = 0
#     b = 1
#     count = 0
#     while count < numb:
#         c = a 
#         a = b
#         b = a + c
#         count += 1
#         print(c, count)
# fib(4)

# def dna_strand(dna):
#     dna_list = list(dna)
#     dna_new = []
#     a = 'T'
#     t = 'A'
#     c = 'G'
#     g = 'C'
#     for elt in dna_list:
#         if elt == "A":
#             dna_new.append(a)
#         elif elt == 'T':
#             dna_new.append(t)
#         elif elt == 'G':
#             dna_new.append(g)
#         else:
#             dna_new.append(c)
#     dna_new = ''.join(dna_new)
#     print(dna_new)

# def dna_join(dna):
#     return ''.join([pairs[x] for x in dna])

# pairs = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
# arr_dna = 'ATGC'
# arr_dna_2 = 'AAAA'
# dna_strand(arr_dna_2)
# print(list(arr_dna))
# print(dna_join(pairs))


# def barista(coffes):
#     time = 0
#     total = 0
#     for elt in sorted(coffes):
#         time += elt
#         total += time
#         time +=2
#     print(total)
# arr = [2,3,9,10,5]
# # arr = [4, 3, 2]
# barista(arr)


# def solve(s):
#     lst = [0, 0, 0, 0]
#     for elt in s:
#         if elt.isupper():
#             lst[0] += 1
#         elif elt.islower():
#             lst[1] += 1
#         elif elt.isdigit():
#             lst[2] += 1
#         else:
#             lst[3] +=1
#     return lst
# symbol = "$Cnl)Sr<7bBW-&qLHI!mY41ODe"
# print(solve(symbol))

# def open_or_senior(data):
#     status = []
#     senior = 'Senior'
#     new = 'Open'
#     for elt in data:
#         if elt[0] >= 55 and elt[1] > 7:
#             status.append(senior)
#         else:
#             status.append(new)
#     print(status)
#     # print(senior,'\n', new)
# arr = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# open_or_senior(arr)
# print(list())

# def solution(*args):
#     new_arr = []
#     if isinstance (*args, list):
#         new_arr = sorted(*args)
#     elif args is None:
#         new_arr = []
#     return new_arr
    

# arr = [1,2,3,10,5]
# print(solution(arr))


# def is_narcissistic(i):
#     b = str(i)
#     a = len(str(i))
#     total = 0
#     for elt in b: 
#         elt = int(elt) ** a
#         total += elt
#     if total == i:
#         return True
#     else:
#         return False
#     #     print(elt, type(elt))
#     # print(total, type(total))
# numb = 407
# print(is_narcissistic(numb))



# def give_change(amount):
#     # emp_arr = [0, 0, 0, 0, 0]
#     arr = []
#     for i in [100, 50, 20, 10, 5, 1]:
#         arr = [amount // i] + arr
#         amount -= arr[0] * i
#         print(arr)
#
# arr = 385
# give_change(arr)

# l = [lambda x: x ** 2,
#      lambda x: x ** 3,
#      lambda x: x ** 4]
# for f in l:
#     print(f(5))
# print(l[1](5))

# key = 'got'
# key_2 = 'one'
# key_3 = 'already'
# dictt = {'already' :(lambda x: x + 2),
#         'got': (lambda: 2 * 4),
#         'one': (lambda: 2 ** 6)}
# print(dictt[key_3](44))
# print(dictt[key]())
#
# lower = (lambda x, y: print(x) if x < y else print(y))
# lower(4,7)
# lower = (lambda x, y: x if x < y else y)
# print(lower(4,3))

# def actions(x):
#         return (lambda z,y: z + y)
# act = actions(99)
# print(act(22, 33))

# actions = (lambda x: (lambda y: x + y))
# act = actions(77)
# print(act(3))


#
# for x in counters:
#         update.append(x + 10)
# print(update)

# def inc(x):
#         return x + 10
# # print(list(map(inc, counters)))
#
# def f(x):
#         return x ** 2
#
# a = [-1, 2, -3, 4, 5]
# c = ['hello', 'hi', 'good morning ept']
# b = list(map(abs, a))
# w = list(map(f, a))
# z = list(map(list, c))
# y = list(map(sorted, c))
# # print(y)
#
# s = list(map(int,input().split()))
# print(s)
# for x in s:
#         print(type(x))
# print(z)
# print(w)
# print(b)

# def bin_to_decimal(inp):
#     # x = list(map(int, inp))
#     # emp = []
#     # for i, elt in enumerate(x[::-1]):
#     #     dig = 0 + 2 ** i * elt
#     #     emp.append(dig)
#     #     print(dig, emp)
#     # return sum(emp)
#     return int(inp, 2)
# inp = "1000000"
#
# print(bin_to_decimal(inp))
# def f(x):
#     return x > 10
#
# a = [12, 0, 5, 79, 645, 7952, 18, 0, 192, 471]
# b = list(filter(f, a))
# print(b)

# for i in range(0, 405, 45):
#     print(i)

# def direction(facing, turn):
#     arr = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
#     return arr[(turn // 45 + arr.index(facing)) % 8]
# print(direction('S', 180))


# def digitize(n):
#     return list(map(int, str(n)[::-1]))


# arr = 548702838394
# print(digitize(arr))



# def last_man_standing(n):
#     a = list(range(1,n+1))
#     while len(a)>1:
#         a = a[1::2][::-1]
#     return a[0]
# print(last_man_standing(9))

# a = [1,2,3,4,5,6,7,8,9]
# b = a[1::2][::-1]
# c = b[1::2][::-1]
# d = c[1::2][::-1]
# print(b,c,d)


# def solve(arr):
#     arr_lett = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m',
#                 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
#     empt_arr = {i + 1: i+1 for i in range(27)}
#     print((empt_arr))

# arr = ["abode","ABc","xyzD"]
# solve(arr)

# letter_count = {chr(i+96):i for i in range(1,27)}

# print(letter_count)

# def unused_digits(*numbers):
#     digt = [i for i in range(10)]
#     empt_arr = str(numbers).split()
#     arr_digit = []
#     for elt in empt_arr:
#         for i in elt:
#             if i.isdigit():
#                 arr_digit.append(int(i))
#     total = list(set(digt) - set(arr_digit))
#     total = sorted([str(i) for i in total])
#     print(''.join(total))


# arr = [2015, 8, 26]

# unused_digits(arr)

# def fact(x):
#     if x == 1:
#         return 1
#     return fact(x -1) * x
#
# print(fact(4))
#
#
# def fib(x):
#     if x == 1:
#         return 1
#     if x == 2:
#         return 1
#     return fib(x-1) + fib(x - 2)
# print(fib(7))


# def palindrom(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return palindrom(s[1:-1])
# print(palindrom('arbra'))


# def rec(x):
#     if len(x) == 1 or len(x) == 2:
#         return x
#     return x[0] + '(' + rec(x[1:-1])  + ')' + x[-1]
#
# stri = 'helloh'
# print(rec(stri))

# def power(x, n):
#     if n ==0:
#         return 1
#     if n % 2 == 0:
#         return power(x, n //2) * power(x, n // 2)
#     else:
#         return power(x, n -1) * x
#
# print(power(2, 10))


# def a(x):
#     if x >= 1:
#         return a(x-1)
#         # print(x - 1, 'before function')
#         # a(x -1)
#         # print(x,'after function')
# a(5)

# def factorial_iterative(num):
#     if num == 1:
#         return num
#     return factorial_iterative(num - 1) * num
#
# print(factorial_iterative(5))

# def mysum(x):
#     print(x)
#     if not x:
#         return 0
#     else:
#         return x.pop(len(x) -1) + mysum(x)
#
# a = [1, 2, 3, 4, 5]
# print(mysum(a))

# def mysum(x):
#     summ = 0
#     while len(x) != 0:
#         summ += x[0]
#         x = x[1:]
#     print(summ)
#
# mysum([1,2,3,4,5])

# def recursive(x):
#     if x < 4:
#         # print(x )
#         recursive(x + 1)
#         print(x, 'after function')
#
# recursive(1)

# def fact(x):
#     if x == 1:
#         return x
#     else:
#         return fact(x - 1) * x
# print(fact(5))
#
# def cicle(d):
#     factorial = 1
#     while d:
#         factorial *= d
#         d -= 1
#         print(factorial)
#
# cicle(5)


# f = {'C':{'Python3.9':['python.exe', 'python.ini'],
#           'Program Files':{
#               'Java':['READMI.txt', 'Welcoe.html', 'java.exe'],
#               'MATLAB':['matlab.bat', 'matlab.exe', 'mcc.bat']
#           },
#           'Windows':{
#               'System32':['acledit.dll', 'aclui.dll', 'zipfldr.dll']
#             }
#           }
#         }
#
#
# def get_files(path, depth=0):
#     for f in path:
#         print(" " *depth, f)
#         if type(path[f]) == dict:
#             get_files(path[f], depth+1)
#         else:
#             print(" " *(depth+1), ' '.join(path[f]))
# get_files(f)


# def rec(string, ch):
#     if not string:
#         return 0
#     elif string[0] == ch:
#         return 1 + rec(string[1:], ch)
#     else:
#         return rec(string[1:], ch)
#
# print(rec('abrasablsdobbqebadoia', 'b'))

# def fib(x):
#     if x == 0:
#         return 0
#     if x == 1:
#         return 1
#     else:
#         return fib(x - 1) + fib(x - 2)
# x = 8
# for i in range(x):
#     print(fib(i), 'dig recur fibo')
#
# def fibonachi(x):
#     a = 0
#     b = 1
#     count = 0
#     while count < x:
#         c = a + b
#         b = a
#         a = c
#         count += 1
#         print(c)
# fibonachi(7)

# def my_sum(x, size):
#     if size == 0:
#         return 0
#     else:
#         return x[size - 1] + my_sum(x, size -1)
# n = int(input('Type len dict: '))
# a = []
# for i in range(0, n):
#     elt = int(input('Type digit: '))
#     a.append(elt)
# print(a)
# # arr = [1,2,3,4,5]
# # print(my_sum(arr, len(arr)))
# print(my_sum(a, n))

# def covert(b):
#     arr = []
#     if b == 0:
#         return arr
#     dig = b % 2
#     arr.append(dig)
#     covert(b // 2)
#     for i in arr:
#         print(i, end='')
# covert(4012)
# arr = []
# def sum_digits(x):
#     if x == 0:
#         return arr
#     dig = x % 10
#     arr.append(dig)
#     sum_digits(x // 10)
#
# sum_digits(546)
# print(sum(arr))
# # print()

# def even(x, result = []):
#     if not x:
#         return
#     else:
#         first = x[0]
#         if first % 2 == 0:
#             result.append(first)
#         even(x[1:])
#         return result
# arr = [i for i in range(1,11)]
# print(arr)
# print(even(arr))

# s = input()
# stack = []
# is_good = True
# for i in s:
#     if i in '({[':
#         stack.append(i)
#     elif i in ')}]':
#         open_bracket = stack.pop()
#         if open_bracket == '(' and i == ')':
#             continue
#         if open_bracket == '{' and i == '}':
#             continue
#         if open_bracket == '[' and i == ']':
#             continue
#         is_good = False
#         break
# print(stack)
# if is_good and len(stack) == 0:
#     print('YES')
# else:
#     print('NO')

# arrow = [1, 2, 99, 88]

"""ВАЖНО РАЗОБРАТЬСЯ! РЕКУРСИЯ"""
# def max_rec(p, arr):
#     if p == len(arr) - 1:
#         return arr[p]
#     max_end = max_rec(p + 1, arr)
#     if arr[p] > max_end:
#         return arr[p]
#     else:
#         return max_end
# print(max_rec(0, arrow))

# def gcd(x, z):
#     if z == 0:
#         return x
#     else:
#         dig = gcd(z, x % z)
#         return dig
# print(gcd(30, 12))

# def simply(x, z=None):
#     if z is None:
#         z = x - 1
#     while z >= 2:
#         if x % z == 0:
#             print('Число не является простым')
#             return False
#         else:
#             return simply(x, z -1)
#     else:
#         print('Число является простым')
#         return True
# print(simply(13))

# def mysum(arr):
#     print(arr)
#     if len(arr) == 1:
#         return arr[0]
#     if not arr:
#         return 0
#     else:
#         return arr[0] + mysum(arr[1:])
#
# arrow = [1,2,3,4,5]
# arrow_2 = ['p', 'r', 'v', 'e', 't']
# #
# # print(mysum(arrow_2))
# # print(mysum(arrow))
# #
# # def total(arr):
# #     summ = 0
# #     while arr:
# #         summ += arr[0]
# #         arr = arr[1:]
# #     print(summ)
# # total(arrow)
# empty = []
# def total(x):
#     if x == 0:
#         return x
#     else:
#         empty.append(x % 10)
#         total(x // 10)
# total(768)
# print(sum(empty))


class Jar():
    def __init__(self):
        self.bank = 0
        self.juices = {}

    def add(self, amount, kind):
        self.bank += amount
        self.juices[kind] = self.juices.get(kind, 0) + amount

    def pour_out(self, amount):
        if amount >= self.bank:
            self.bank = 0
            for k, v in self.juices.items():
                self.juices[k] = 0
        else:
            self.bank -= amount
            for k, v in self.juices.items():
                if len(self.juices) == 1:
                    self.juices[k] = self.juices.get(k, 0) - amount
                else:
                    self.juices[k] = self.juices.get(k, 0) - amount / 2
            return self.juices[k]

    def get_total_amount(self):
        return self.bank

    def get_concentration(self, kind):
        if kind not in self.juices or self.bank == 0:
            return 0
        else:
            return self.juices.get(kind, 0) / self.bank * 100 / 100

j_1 = Jar()
# j_1.add(100, 'apple')
# j_1.add(200, 'banana')
# j_1.add(200, 'banana')
print(j_1.__dict__)
print(j_1.get_concentration('apple'))
# j_1.add(100, 'apple')
# j_1.pour_out(400)
print(j_1.__dict__)
print(j_1.get_concentration('apple'))
# print(j_1.get_concentration('banana'))

