import time
import functools
import asyncio
from time import sleep
from functools import lru_cache, wraps

#
def cache(func):
    '''Кэширует результаты выполнения функции
    Для кэша используется атрибут cache функции wrapper'''
    @functools.wraps(func)
    def wrapper(*args):
        cache_key = args
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args)
        return wrapper.cache[cache_key]

    wrapper.cache = dict()
    return wrapper

@cache
def fibonacci(num):
    ''' Вычисляет число Фибоначчи'''
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

x = fibonacci(10)
print(x)
assert x is fibonacci(10)
sleep(6)
assert x is not fibonacci(10)
# def caching_lr(second: int):
#     def wrapper_cache(func):
#
#
# while retries < timeout:
#     value = func(*args)
#     print(f"Сон на {timeout} секунды")
#     time.sleep(timeout)
#     retries += 1

# def caching(timeout):
#     def real_decorator(func):
#         def wrapper(*args):
#             value = func(*args)
#             tries = 1
#             while tries < timeout:
#                 print(f"You tries is {tries}")
#                 # time.sleep(4)
#                 for key in value:
#                     value[key] = key + 1
#                     print(key)
#                 tries += 1
#
#
#             return value
#         return wrapper
#     return real_decorator
#
#
# @caching(timeout=3)
# def func(x):
#     return {x:42}
#
# x = func(2)
# print(x)
# assert x is func(2)
# assert x != func(2)

# x = {2: 41}
# print(x)
# x[2] += 2
# print(x)



# def timer(func):
#     '''Выводит время, затраченное на выполнение функции
#     '''
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         run_time = end_time - start_time
#         print("Выполнение функции заняло {run_time:.4f} секунд".format(run_time=run_time))
#         return value
#     return wrapper
#
#
# @timer
# def fibonacci(num):
#     ''' Вычисляет число Фибоначчи
#     '''
#     if num < 2:
#         return num
#     return fibonacci(num - 1) + fibonacci(num - 2)
#
#
# fibonacci(10)

# fibonacci(30)
