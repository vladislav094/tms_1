# Tasks 3
# Types data

var_int = 10
var_float = 8.3
var_str = 'No'
var_str_yes = 'Yes'
big_int = var_int * 3.5
var_float = var_float - 1.0
var_str = var_str + var_str + var_str_yes * 4
print(var_int / var_float)
print(big_int / var_float)
print(big_int)
print(var_float)
print(var_str)

# String

#1 
variable_str = 'Zxcvbnmqwe'
print(variable_str[0])
print(variable_str[-1])
print(variable_str[2])
print(variable_str[-3])
print(len(variable_str))

#2
variable_str_2 = 'HelloWorldMyNameIsGoodvin'
print(variable_str_2[0:8])
print(len(variable_str_2))
print(variable_str_2[12:16])
print(variable_str_2[::3])
print(variable_str_2[::-1])

#3
name = 'Vlad'
my_name = 'My name is ' + name
print(my_name)

#4
test_tring = 'Hello world!'
print(test_tring.find('w'))
print(variable_str_2.count('l'))
print(variable_str_2.startswith('Hello'))
print(variable_str_2.endswith('qwe'))


# HW_3

#1
string = 'www.my_site.com#about'
correct_string = string.replace('#', '/')
print(string)
print(correct_string)

#2 v1  
text = ['items', 'lists', 'words', 'books', '']
print('ing '.join(text))
print(' ')

#2 v2
words = 'items', 'lists', 'words', 'books'
result = 'ing '.join(words)
print(result)


#3 v1
full_name = 'Ivanou Ivan'
first_name = full_name[:full_name.find(' ')]
second_name = full_name[full_name.find(' ')+1:]
print(full_name)
print(second_name, first_name)
print(' ')

#3 v2 (list in result)
full_name = 'Ivanou Ivan'
change_word = full_name.split()
change_word.reverse()
print(full_name)
print('Full name:', change_word)
print(' ')

#4
words = ' It"s simple text with space between words '
print(words)
words = words.strip()
print(words)




