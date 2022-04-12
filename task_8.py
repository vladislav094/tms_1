"""1"""
def decorator(func):
	def wrapper(*args):
		func(*args)
		for elt in args[:]:
			elt += 1
			print(elt)
	return wrapper

@decorator
def plus_one(*args):
	return args

@decorator
def plus_to_str(*args):
	return args
plus_one(3, 33)

"""2"""
# def up_text(func):
#     def wrapper(*args):
#         func(*args)
#     return wrapper

# @up_text
# def my_text():
#     text = input(f'Please, type word in the field: ')
#     print(text.upper())


"""3"""
def change(func):
    def wrapper(*args):
        return func(*args[::-1])
    return wrapper

@change
def numbers(*args):
    print(args)

numbers(1, 2, 3, 42, 5)
numbers('Hello world!', 123, 'qweqwe')

"""4"""
numbers = ['1 2 3 4 5 6 7 8 9 10 11 12 13']
number_names = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8:
				'eight', 9: 'nine',
				10: 'ten', 11: 'eleven', 12: 'twelve',
				13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18:
				'eighteen', 19: 'nineteen'}

def decorator(func):
	def wrapper(*args, **kwargs):
		func(*args, **kwargs)
		result = []
		arg = args[0]
		arg_1 = args[1]
		arg_0 = ' '.join(map(str, arg))
		for elt in arg_0.split():
			result.append((elt, arg_1[int(elt)]))
		print(f"До сортировки {result}")
		print(f"После сортировки", *sorted(result, key=lambda x: x[1]))
	return wrapper

@decorator
def sorted_by_up(*args):
	return args
sorted_by_up(numbers, number_names)

