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




class Country:
    # men_count = "I'm the default"

    def __init__(self, demographics):
        # print(self.demographics)
        self.demographics = demographics
        print(self.demographics)

    # @property
    # def demographics(self):
    #     return self.demographics

    # @demographics.setter
    # def demographics(self, birth_rate):
    #     print(self.demographics, self.men_count, birth_rate)
    #     self.men_count = self.demographics * birth_rate

c = Country(0.3)
# c()
# c.demographics











class Men:

    age = 11
    name = 'Ivan'
    country = 'Italy'

    def __init__(self, second_name, course):
        self.second_name = second_name
        self.course = course


    @classmethod
    def add_fio(cls):
        return cls.second_name

    @staticmethod


print(Men.age)
# m = Men('Ivanov', 456)
# print(m)











