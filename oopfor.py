# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#
#     def get_grade(self):
#         return self.grade
#
# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []
#
#     def add_students(self, students):
#         if len(self.students) < self.max_students:
#             self.students.append(students)
#             return True
#         return False
#
#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#
#         return value / len(self.students)
#
# s1 = Student('Tom', 19, 95)
# s2 = Student('Bill', 19, 75)
# s3 = Student('Fred', 19, 65)
#
# course = Course('Science', 3)
# course.add_students(s1)
# course.add_students(s2)
# course.add_students(s3)
# print(course.add_students(s2))
# print(course.get_average_grade())

# class Person:
#     number_of_people = 0
#
#     def __init__(self, name):
#         self.name = name
#         Person.add_person()
#     @classmethod
#     def number_of_people_(cls):
#         return cls.number_of_people
#
#     @classmethod
#     def add_person(cls):
#         cls.number_of_people += 1
#
#
# p1 = Person('Jim')
# p2 = Person('Fredd')
# p3 = Person('Bobby')
# print(Person.number_of_people_())



# class A:
#     def a(self):
#         print('A')
#
# class B:
#     def a(self):
#         print('B')
#
# class C(B):
#     def a(self):
#         print('C')
#
# class D(C, A):
#     def a(self):
#         super(C, self).a()
#         print(self.__class__.__mro__)
#
# # print(D.__mro__)
# D().a()

# class Banck:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def get_balance(self):
#         print(self.balance)
#         return self.balance
#
#     def set_balance(self, value):
#         print(self.balance + value)
#         self.balance = self.balance + value
#         return self.balance
#
#     my_balance = property()
#     my_balance = my_balance.getter(get_balance)
#     my_balance = my_balance.setter(set_balance)
#     # my_balance = my_balance.deleter(del_balancr)
#
# a1 = Banck('Ivan', 123)
# print(a1.__dict__)
#
# a1.my_balance
# a1.my_balance = 1000
# a1.my_balance

# def header(func):
#     def inner(*args):
#         print('<h1>')
#         func(*args)
#         print('/<h1>')
#     return inner
#
# def table(func):
#     def inner(*args):
#         print('<table>')
#         func(*args)
#         print('/<table>')
#     return inner
#
# @table
# @header
# def say(name, surname):
#     print('Hello World!', name, surname)
#
# def buy():
#     print('buy world!')
# say('Piotr', 'Ivanov')

def average_numbers():
    value = 0
    count = 0
    def inner(number):
        nonlocal value, count
        value = value + number
        count = count + 1
        print(value, count)
        return value / count
    print(inner)
    return inner

r1 = average_numbers()
r1(1)
r1(5)
r1(13)
print(average_numbers)



