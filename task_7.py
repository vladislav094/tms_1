#1
list_peoples = [165, 163, 161, 160, 157, 157, 155, 154]
x = 162
def rank():
    """
    Функция проверяет элементы списка и добавляет "x" после элемента с
    таким же значением, выводит место (индекс) объекта "x"
    """
    for i, elt in enumerate(list_peoples):
        if x < elt:
            print(f"Номер: {i + 1}")
            list_peoples.insert(i + 1, x)
            print(list_peoples)
            break
        elif x > elt:
            list_peoples.insert(i, x)
            print(list_peoples)
            break
rank()
# print(rank())
# #2
# a = [1, 5, 2, 4, 3]
# b = [1, 2, 3, 4, 5]
# arr_result = []
# def numbers(x):
#     """Функция перебирает элементы массива и добавляет в пустой масив те элементы,
#     которые больше (по значению) предыдущего элемента"""
#     # for elem in range(len(x) - 1):
#     #     n = x[elem]
#     #     elem += 1
#     #     m = x[elem]
#     #     if m > n:
#     #         arr_result.append(m)
#     # print(arr_result)
#     """v2 Лаконичный вариант"""
#     for i in range(len(x)- 1):
#         if x[i] < x[i + 1]:
#             arr_result.append(x[i + 1])
#     print(arr_result)
#     """v3 Вывод элементов по условию (больше прыудщего)
#        без добавления в массив"""
    # for i in range(1, len(x)):
    #     if x[i] > x[i -1]:
    #         print(x[i])
    # print(arr_result)
# numbers(b)

# #3
a = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 12]]
b = [1, 2, [3, 4, [5, 6], 7], [8, [9, [10]]]]
c = []
"""Рекурсивный метод сглаживания двумерного списка"""
# def flattenlist(arr):
#     if len(arr) == 0: #Если длина вложенного списка равна нулю - возвращаем вложенный список
#         return arr
#     if isinstance(arr[0], list): #Если элемент в нулевом индексе является экземпляром списка,
#                                  # то индекс списка снова входит в функцию и добавляется к след индексу и т.д
#         return flattenlist(arr[0]) + flattenlist(arr[1:])
#     return arr[:1] + flattenlist(arr[1:])
def fla(arr):
    """Функция принимает все элементы вложенных списков и добавляет их в отдельный список """
    for i in arr:
        if type(i) == list:
            fla(i)
        else:
            c.append(i)
    return c
# def number(arr):
#     """Функция перебирает элементы списка, элементы вложенных списков и 
#     добавляет каждый элемент в новый список
#     """
#     for elt in arr:
#         if isinstance(elt, list):
#             for item in elt:
#                 c.append(item)
#         else:
#             c.append(elt)
#     print(c)
print(fla(b))
# print(flattenlist(x))