# d = {'EUR': 2, 'USD': 0.75, 'BYN': 0.32, 'CAD': 1.23, 'RUB': 0.12}
# for k, v in d.items():
#     print(k + 'qwe')


from cgi import test


var_int = 10
var_float = 8.4
var_str = 'No'
var_str_2 = 'Yes'
big_int = var_int * 3
var_float = var_float - 1
print(var_float)
print(round(var_int / var_float, 2))
print(round(big_int / var_float, 2))
var_str = var_str * 2 + var_str_2 * 4
print(var_str)
print(var_int)
print(big_int)

var_text = 'HelloMyDearFriend'
print(var_text[:1])
print(var_text[-1:])
print(var_text[2])
print(var_text[-3])
print(len(var_text))

var_random = 'LondonIsTheCapitalOfrGreatBritains'
print(var_random[0:8])
var_rand_2 = int(len(var_random) / 2)
print(var_rand_2)
print(var_random[(var_rand_2 - 2) : (var_rand_2 + 2)])
print(var_random[::3])
print(var_random[::-1]) 

name = 'My name is'
first = 'Bobby'
print(f"{name} {first}")
test_string = 'Hello world!'
print(test_string.find('w'))
print(test_string.count("l"))
print(test_string)