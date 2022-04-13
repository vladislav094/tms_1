# """1"""
# class Employee:
#     count = 0
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.count += 1

#     def show_name(self):
#         print(f"Name: {self.name}")

#     def show_count(self):
#         print(f"On current time in company have {Employee.count} employee")

# emp1 = Employee('Nick', 1440)
# emp2 = Employee('Madman', 1280)
# emp3 = Employee('Madman1', 51280)

# emp1.show_name()
# emp2.show_name()
# emp2.show_count()


# """2"""
# class Students:
#     def __init__(self, second_name, fio, group_num, avg_grade=None):
#         self.second_name = second_name
#         self.fio = fio
#         self.group_num = group_num
#         self.avg_grade = avg_grade

# class School:
#     student_list = []

#     @classmethod
#     def add_student(cls, student):
#         cls.student_list.extend(student)
#         # for student in cls.student_list:
#             # print(student.second_name)

#     @classmethod
#     def show_second_name(cls):
#         for student in cls.student_list:
#             if student.avg_grade in [5, 6]:
#                 print(student.second_name, student.group_num)

#     @classmethod
#     def show_student_group(cls, group):
#         for student in cls.student_list:
#             if student.group_num == group:
#                 print(student.second_name, student.fio)

#     @classmethod
#     def show_student_avg_grade(cls,grade):
#         for student in cls.student_list:
#             if student.avg_grade >= grade:
#                 print(f"{student.second_name} have grade >= {grade}")


# s1 = Students('Ivan', 'III', 123, 5)
# s2 = Students('Petr', 'PPP', 456, 7)
# s3 = Students('Sergey', 'SSS', 789, 6)
# s4 = Students('Fedor', 'FFF', 123, 6)
# s5 = Students('Tihon', 'TTT', 623, 5)


# sch = School()
# sch.add_student([s1, s2, s3, s4])

# sch.show_second_name()
# sch.show_student_group(123)
# sch.show_student_avg_grade(7)

"""3"""
# class Students:
#     student_list = []

#     def __init__(self, name, money):
#         self.name = name
#         self.money = money

#     @staticmethod
#     def show_money(student):
#         for elt in student:
#             student_money = elt.money
#             student_name = elt.name
#             Students.student_list.append(student_money)
#             max_money = max(Students.student_list)
#         print(max_money, student_name)

# s1 = Students('Ivan', 456)
# s2 = Students('Petr', 723)
# s3 = Students('Sergey', 111)
# s4 = Students('Igor', 724)
# Students.show_money([s1, s2, s3, s4])



# class TriangleChecker:
#     def __init__(self, sides):
#         self.sides = sides

#     def is_triangle(self):
#         if all(isinstance(side, int) for side in self.sides):
#             if all(side > 0 for side in self.sides):
#                 sorted_sides = sorted(self.sides)
#                 if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
#                     return print('Ура, можно построить треугольник!')
#                 return print('Жаль, но из этого треугольник не сделать')
#             return print('С отрицательными числами ничего не выйдет!')
#         return print('Нужно вводить только числа!')
# tr = TriangleChecker(4)
# tr.is_triangle()

# """4"""
# from dataclasses import dataclass
# # @dataclass
# class Country:
#     men_count = None
#
#     @property
#     def population(self):
#         return self.count
#
#     @population.setter
#     def population(self, birth_rate):
#         return self.men_count * birth_rate
#
# @dataclass
# class Russia(Country):
#     men_count = 142_000_000
#
# @dataclass
# class Germany(Country):
#     men_count = 68_000_000
#
# r = Russia()
# g = Germany()
# r.population
# g.population
# g.population(bith_rate=3)


class Shop:
    all_price = []
    def __init__(self, item, price):
        self.item = item
        self._price = price
        self.all_price.append(self._price)

    @property
    def add_price(self):
        return self._price

    @add_price.setter
    def add_price(self, value):
        self.all_price.append(value)

    @classmethod
    def sum_overall_price(cls):
        return sum(cls.all_price)

s1 = Shop('Book', 1234)
s2 = Shop('Newspaper', 31)
s3 = Shop('Pencil', 41)
s1.add_price = 441
s2.add_price = 100
s3.add_price = 78
print(Shop.all_price)
print(s1.item, s1._price)
print(Shop.sum_overall_price())



    