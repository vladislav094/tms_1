# 1
from attr import frozen


string = 'Robin Singh'
arr1 = string.split()
print(arr1)

string_2 = 'I love arrays they are my favorite'
arr2 = string_2.split(' ')
print(arr2)

# 2
name = ['Ivan', 'Ivanov']
# string_name = str(name)
string_name = ' '.join(name)
print(string_name)
city = 'Minsk'
country = 'Belarus'
print(f"Hello, {' '.join(name)}! Welcome in {city} {country}")

# 3
arr3 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(' '.join(arr3))

#4
arr4 = ['One', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight',
        ' nine', 'ten']

arr4.insert(2, 'Dubb')
del arr4[6]
print(arr4)

#5
a = { 'a': 1, 'b': 2, 'c': 3}
b = { 'c': 3, 'd': 4,'e': 5}
c = { 'v': 3, 't': 4,'e': 5}
dict_c = {**a, **b}
for key in dict_c:
    dict_c[key]=[a.get(key),b.get(key)]
print(dict_c)

#*1
arr_int = [1, 5, 2, 9, 2, 9, 1, 1, 1]
arr_list = [i for i in arr_int if arr_int.count(i) == 1]
print(arr_list)

#*2.1        
text = 'Hello World!'
text_a = {}
r = 0
for i in text:
    text_a[i] = text_a.get(i, 0) + 1
print(text_a)
for k in text_a:
    if text_a[k] > r:
        r = text_a[k]
        m = k
print(f"{text}=={m}")

# 2й способ добавления строки в словарь 
# text_b = {}
# for i in text:
#     if i in text_b:
#         text_b[i] += 1
#     else:
#         text_b[i] = 1
# print(text_b)