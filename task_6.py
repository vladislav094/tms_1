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
# pi = 'global'

# def inner():
#     pi = 'local'
#     # print(pi)
# print(pi)

# #3
# def outer_hello():
#     print('Hello')
#     def inner_hello():
#         print('World!')
#     inner_hello()
# outer_hello()
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
    



# def counter():
#     count = 1 
#     def inner():
#         """"
#         Функция обращается к переменной внешней функции (counter), прибавляет к значению переменной
#         (count) +1 и возвращает значение в функцию inner. Во внешней функции (counter) возвращается 
#         значение вложенной функции inner
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
#     Цикл вызывает функцию counter обращаясь к переменной 'q', 
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




def outer_func(x):
    def inner_func(y):
        return y + x
    return inner_func

x = outer_func(hex(id(2)))
print(x(5))