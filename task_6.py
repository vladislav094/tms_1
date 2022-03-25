# Функции 
# #1 
# def hello():
#     print(f"Hello World!")
# hello()



# #2
# def sum_numbers(a, b, c):
#     x = a + b + c
#     print(x)
#     # return x
# sum_numbers(2, 3, 7)



# #3 v1
# def outer_hello():
#     print('Hello')
#     def inner_hello():
#         print('World!')
#     inner_hello()
# outer_hello()

# # #3 v2
# def outer_func(a, b):
#     def inner_func():
#         if a >= 3 and b >=4:
#             print(a * b)
#         else:
#             pass
#     inner_func()
# outer_func(4, 5)



# #4
# def reversed1():
#     """
#     Внешняя функция, которая сохраняет число в переменной "n1"
#     и проверяет число в соответствии с инструкциями if, elif
#     и помещает данные из перменной "n1" в переменну vari
#     """
#     n1 = int(input(f"Введите число: "))
#     if n1 < 0:
#         print(f"Число не должно быть отрицательным")
#     elif n1 > 0:
#         vari = str(n1)
# #     def reversed_inner(vari):
# #         """
# #         Внутренняя функция, которая циклом перебирает каждый элемент
# #         из переменной vari и в соответствии с условиями помещает в 
# #         переменную "res". Вовзращает результат в функцию reversed_inner
# #         """
# #         res = ''
# #         for i in range(len(vari)-1, -1, -1):
# #             res = res + vari[i]
# #         return res
#     """
#     Ещё один способ, который позволяет выполнить условие рекурсией
#     """
#     def reversed3(vari):
#         """
#         Функция, которая разворачивает число рекурсией.
#         """
#         if len(vari) == 1:
#             return vari
#         return vari[-1] + reversed3(vari[:-1])

#     # print(reversed_inner(vari))    
#     print(reversed3(vari))
# n = reversed1
# n()



# #5
# def fib():
#     """Функция возращает n-е число Фибоначчи по числу указанному при вводе или агрументе """
#     n = int(input(f"Введите число: "))
#     i = 0
#     number = 20 
#     second = 1
#     if n >  0:
#         while i <= number:
#             if (i <= 1):
#                 next = n 
#             else:
#                 next = n + second 
#                 n = second 
#                 second = next 
#             print(next)
#             i += 1
# fib()



# #6
# def palindrome():
#     """Функция (является ли слово/фраза палиндромом),которая переворачивает символы из переменной "n"
#     и добавляет в переменную "s", удаляет лишние символы(пробелы),
#     и затем сравненивает (==) переменные. Выводит результат в 
#     зависимости от соблюдения условий.
#     """
#     n = list(input(f"Введите слово или фразу: "))
#     s = n[::-1]
#     for i in s:
#         if i == ' ':
#             s.remove(i)
#     for i in n:
#         if i == ' ':
#             n.remove(' ')
#     print(f"n = {n}")
#     print(f"s = {s}")
#     # print(f"x = {x}")
#     if s == n:
#         print(True)
#     else:
#         print(False)
# palindrome()


# #7
# def check_coupon(entered_code, correct_code, current_date, expiration_date):
#     a = 123

def check_password():
    username = input(f"Введите имя: ")
    password = input(f"Введите пароль: ")
    if len(password) < 8:
        print(f"Пароль слишком короткий")
        return False
    elif username in password:
        print(f"Пароль содержит имя пользователя")
        return False
    else:
        print(f"Пароль для пользователя {username} порошёл все проверки")
        return True

check_password()





# list_1 = ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"] 
# exclude = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

# def filter_list():
#     """Функция выполняет фильтр двух списков, удаляет дубли и возвзращает уникальные элементы в новом списке"""
#     new_list = []
#     for i in list_1[:]: 
#         """Указываем срез [:] для повторения итерации цикла с 0 индекса"""
#         if i not in exclude:
#             new_list.append(i)
#         else:
#             list_1.remove(i)
#     return new_list
# print(filter_list())    











# """
# Цикл вовзращает число наоборот 
# """
# n1 = int(input("Введите число: "))
# n2 = 0
# while(n1 > 0):
#     dig = n1 % 10
#     n1 = n1 // 10 
#     n2 = n2 * 10
#     n2 = n2 + dig
# print(n2)
    


# """Функция "counter" и цикл "while" """
# def counter():
#     count = 1 
#     def inner():
#         """"
#         Функция "inner" обращается к переменной внешней функции "counter",
#         прибавляет к значению переменной "count" +1 и возвращает значение 
#         в функцию inner. Во внешней функции "counter" возвращается 
#         значение вложенной функции "inner"
#         """
#         nonlocal count 
#         count +=1
#         return count 
#     return inner
# q = counter()
# num = 16
# i = 0
# while i <= num:
#     """
#     Цикл вызывает функцию "counter" обращаясь к переменной "q", 
#     т.к функциия хранится в памяти перменной
#     и выводит результаты функции на экран 
#     """
#     print(q())
#     i += 1




# def factorical(number):
#     if not isinstance(number, int):
#         raise TypeError('Число должно быть целым.')
#     if number < 0:
#         raise ValueError('Число должно быть неотрицательным.')
#     def inner_factorical(number):
#         if number <= 1:
#             return 1
#         return number * inner_factorical(number -1)
#     return inner_factorical(number)    
# print(factorical(4))




# def outer_func(x):
#     def inner_func(y):
#         return y + x
#     print(hex(id(inner_func)))
#     return inner_func
# print(hex(id(outer_func)))
# x = outer_func(2)
# print(outer_func(2))
# print(x(5))