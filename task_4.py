# Task_4 
# List
#1
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
# arr6 = arr5[::3] 
arr6 = arr5[0:7:3]
print(arr6)
#6 v1
arr7 = ['one', 'two']
arr6.extend(arr7)
# arr6.append('blablacar')
# print(arr6)
# arr6.append('magazine')
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
print(arr_a_b, 1)
#7 v2
# It is example cycle for future
# arr_a_b = []
# for i in a:
#     if i in b:
#         arr_a_b.append(i)
#8
new_arr = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
new_arr_set = list(set(new_arr))
print(new_arr_set)

# Logical operators
#1
first = 2201
second = 1745
#2
# first part with AND
if first > 1000 and second > 1000 and 2 + first >= 2203 and second + 5 >= 1750:
    print(True, 1)
if first - second > 0 and second - first < 0:
    print(True, 2)
# second part with AND
if first > second and second > first:
    print(True, 3)
else:
    print(False, 3)
if first + second / 3 == 312 and first - second + 44 == 312:
    print(True, 4)
else:
    print(False, 4)
#3 
# first part with OR
if first + second == 1 or first * second > 0:
    print(True, 5)
else:
    print(False, 5)
if ((first * 2) + (second * 2) == 7892) or ((first * 2) + (second * 2) == 7893):
    print(True, 6)
else:
    print(False, 6)
# second part with OR
if first * 2 + first / 2 <= first * 2 + first / 4 or first + second == 3940 + 62:
    print(True, 7)
else:
    print(False, 7)
if (first + second) / 2 + (first / 3 + second * 2.2) <= 1328 or first / second + 22 == 1388:
    print(True, 8)
else:
    print(False, 8)
#4 
a = 'str'
b = 'ing'
c = 'pass'
d = 'word'
a_b = 'string'
c_d = 'password'
if ((a + b) == ('string' or c + d) == 'pasword'):
    print(True, 9)
else:
    print(False, 9)
if a + b == 'teach' and c + d == 'pasword':
    print(True, 10)
else:
    print(False, 10)
if a + b == a_b and c + d == c_d:
    print(True, 11)
else:
    print(False, 11)

# Dictionary
school = {'1a': 17, '2b': 22, '3f': 9,
          '4d': 25, '5n': 11, '6c': '28',
          '7g': 7, '8a': 13 , '9c': 10,
          '10w': 21}
print(school)
print(school['1a'])
school_1 = school.fromkeys(['2b', '5n', '3f'], 41)
print('fromkeys for school', school_1) 
school.update({'1a': 121, '4d': 2, '8a': 118})
print(school)
school.update({'44z': 228})
print(school)
school['23sh']= 8
print(school)
school.pop('23sh')
del school['44z']
print(school)



