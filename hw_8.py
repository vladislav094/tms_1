"""1"""
def typed(type_):
    """Декоратор выполняет проверку и конвертацию данных"""
    def real_typed(_):
        def wrapper(*args):            
            if type_ == str:
                return ''.join(map(str,args))
            elif type_ == int:
                return sum(map(int, args))
        return wrapper
    return real_typed

 
@typed(str)
def add_two_symbols(*args):
    return args
print(add_two_symbols('3', 5, 'a', 'b', 123))
print(add_two_symbols(5, 5, 123))

@typed(int)
def add_three_symbols(*args):
    return args

print(add_three_symbols(5, 7, '12', 123, '222'))

