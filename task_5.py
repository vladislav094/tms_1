# IF 
# 1
# a = int(input(f"Введите число: " ))
# if a > 0:
#     print(f"Переменная больше 0")
# if a < 0:
#     print(f"Переменная меньше 0")
# # 2
# b = int(input(f"1 or -1. Введите число: "))
# if b > 0:
#     print(1)
# else:
#     print(-1)
# 3
# c = int(input(f"If-elif-else. Введите число: "))
# c_2 = 0
# if c < 10:
#     c_2 = c + 1
# elif c >= 10 and c <= 20:
#     c_2 = (c + 1) * 2
# elif c >= 20 and c <= 30:
#     c_2 = (c + 1) * 3
# else:
#     c_2 = (c + 1) * 4
# print(f"Ваше число = {c_2}")

# ELIF
# 1, a 
# d = int(input(f"Введите число: "))
# e = int(input(f"Введите второе число: "))
# # b
# if d > e:
#     f = d - e
# # c
# elif d < e:
#     f =  d + e
# # d
# else:
#     f = d 
# # e
# print(f)
# 2
# my_list = ['Brad', 'Tom', 'Allan', 'Cris']
# for i in my_list:
#     """"Этот цикл добавляет символ '-' в конце каждой буквы и выводит на экране в одну строку"""
#     for a in i:
#         print(a, end = '-')
# 3
# int_List = [2, 4, 6, 8, 10 ]
# for i in int_List:
#     x = float(i)
#     print(type(x), x)

# WHILE
# 1
i = 0 
number = 21
first = 1
second = 1
lists = []
while i <= number:
    if (i <= 1):
        next = first
    else:
        next = first + second
        # print( first, second, next)
        first = second 
        second = next
        """"Метод append добавляет в список list полученные значения из переменной next"""
        lists.append(next)
    print(next)
    i += 1
# print(lists[4:])

# 2
# i = 0 
# num = 20
# while i <= num:
#     if i % 2 == 0:
#         """"Цикл выводит чётные числа от 0 до 20"""
#         print(i)
#     i +=1
    
# 3
# i = -1 
# num = -21
# while i >= num:
#     """"Цикл выводит каждое третье число от -1 до -21 """
#     if i // i == 1:
#         print(i)
#     i -= 2

# zero = []
# several_likes = ['Ant', 'Few', 'Quz', 'Sum']
# one_like = ['Toddy']
# two_like = ['Bobby', 'Taty']
# three = ['Kino', 'Few', 'Quz']

# def likes_counter(x):
# """
# Эта функция выводит кол-во лайков
# """
#     if len(x) == 0:
#         print('no one like this')
#     elif len(x) == 1:
#         print(f"{x[0]} like this")
#     elif len(x) == 2:
#         print(f"{x[0]} and {x[1]} like this")
#     elif len(x) == 3:
#         print(f"{x[0]}, {x[1]} and {x[2]} like this")
#     else:
#         print(f"{x[0]}, {x[1]} and {len(x)-2} other like this")

# likes_counter(three)

# def duplicate(element: str, count: int) -> bool:
#     return count * element
# duplicate(4, 3)
# print(duplicate('a', 3))
