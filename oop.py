# Объект - сущность, объединяющая данные и методы для работы с ними (состояние и методы)
# Класс - новый тип данных, объект - его конкретный представитель
# Чертёж = класс, дом = объект
# У любого объекта есть id и тип
# Первая потребность для классов - когда не хватает встроенных типов
# Метод - это функция которая принадлежит классу 
# Dunder (дандер), магический метод 

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#
#     def meow(self):
#         print(f'{self.name} says: Meow!')
#
#     def old(self):
#         print(f'{self.name} says: Me', self.age ,'years!')
#
#     def name_friend(self):
#         print(f'{self.name} says: Hello', angela.name)
#
#
# if __name__ == '__main__':
#     tom = Cat('Tom', 2)
#     angela = Cat('Angela', 1)
#     print(tom)
#     print(angela)
#     tom.meow()
#     angela.meow()
#     tom.old()
#     angela.old()
#     tom.name_friend()

# class Students:
#
#     def __init__(self, second_name, fio, group_num, avg_grade):
#         self.second_name = second_name
#         self.fio = fio
#         self.group_num = group_num
#         self.avg_grade = avg_grade
#
# class School:
#     student_list = []
#     @classmethod
#     def add_student(cls, student):
#         cls.student_list.append(student)


class FirstClass:
    def set_data(self, value):
        # self.data = 1
        self.data = value

    def display(self):
        print(self.data)


class SecondClass(FirstClass):
    def display(self):
        print(f"Current value = {self.data}")

class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        # pass
        return f"[ThirdCLass: {self.data}]"

    def __mul__(self, other):
        self.data *= other

    def add_count(self, other):
        self.data *= other
        return self.data

class Rec:
    pass

Rec.name = 'Bob'
Rec.age = 40
print(Rec.name)
y = Rec()
x = ThirdClass(123)
x.display()
print(x)
x.name = 'Sue'
print(x.__dict__, y.__dict__)
print(x.name, y.name)
print(list(Rec.__dict__.keys()))

