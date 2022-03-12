# Task_4 
# List
#1
from hashlib import new
from xmlrpc.client import Boolean


arr1 = ['abc', 'cba', 'qwe', 'abra', 'asd']
arr2 = ['zxc', 'csq', 'adq', 'asqw', 'sdx']
arr3 = [1, 2, 3, 4, 5]
arr4 = [6, 7, 8, 9, 10]
#2
print(arr1[1])
#3
arr2[-1] = 'focus'
print(arr1)
print(arr2)
#4
arr5 = arr1 + arr2
print(arr5)
#5
arr6 = arr5[::3]
print(arr6)
#6 v1
arr6.append('blablacar')
arr6.append('magazine')
print(arr6)
#6 v2
arr6.insert(3,'STQB')
arr6.insert(5, 'BBQ')
print(arr6)
#6 v3.0
arr_add = ['proton', 'texture']
arr6.extend(arr_add)
print(arr6)
#6 v3.1
arr6.extend(['example', 'rule'])
print(arr6)
#7
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
arr_a_b = list(set(a) & set(b))
print(arr_a_b)
#7 v2
# It is example cycle for future
# arr_a_b = []
# for i in a:
#     if i in b:
#         arr_a_b.append(i)
#8
new_arr = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
new_arr = list(set(new_arr))
print(new_arr)

# Logical operators
#1
first = 2201
second = 1745
#2
# first part with AND
if first > 1000 and second > 1000 and 2 + first >= 2203 and second + 5 >= 1750:
    print(True)
if first - second > 0 and second - first < 0:
    print(True)
# second part    
if first > second and second > first:
    print(True)
else:
    print(False)
if first + second / 3 == 312 and first - second + 44 == 312:
    print(True)
else:
    print(False)
#3 
# first part with OR
if first * 2 + first / 2 <= first * 2 + first / 4 or first + second == 3940 + 6:
    print(True)



