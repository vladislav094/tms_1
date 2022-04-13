"""1"""
# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old

#     @property
#     def old(self):
#         return self.__old
    
#     @old.setter
#     def old(self, old):
#         self.__old = old

#     @old.deleter
#     def old(self):
#         del self.__old

# p = Person('Ivan', 20)
# # p.set_old(35)
# # print(p.old)
# # a = p.old
# # p.__dict__['old'] = 'old in p'
# # p.old = 35
# print(p.old, p.__dict__)
# p.old = 35
# del p.old
# # print(p.old, p.__dict__)
# print(p.__dict__)
# p.old = 22
# print(p.old, p.__dict__)



"""2"""
# from string import ascii_letters
#
# class Person:
#     S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
#     S_RUS_UPPER = S_RUS.upper()
#
#     def __init__(self, fio, old, ps, weight):
#         self.verify_fio(fio)
#         self.verify_old(old)
#         self.verify_ps(ps)
#         self.verify_weight(weight)
#
#         self.__fio = fio.split()
#         self.__old = old
#         self.__passport = ps
#         self.__weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if type(fio) != str:
#             raise TypeError(f"FIO must be string")
#
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError(f'incorrect format data')
#         letters = ascii_letters +cls.S_RUS + cls.S_RUS_UPPER
#         for s in f:
#             if len(s) < 1:
#                 raise TypeError(f"Must be one symbol")
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("FIO must be use only letters")
#
#     @classmethod
#     def verify_old(cls, old):
#         if type(old) != int or old < 14 or old > 120:
#             raise TypeError(f"Old must be > 14 and < 120")
#
#     @classmethod
#     def verify_weight(cls, weight):
#         if type(weight) != float or weight < 20:
#             raise TypeError(f"Weight must be float an > 20")
#
#     @classmethod
#     def verify_ps(cls, ps):
#         if type(ps) != str:
#             raise TypeError(f"PS must be a string")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError(f"Wrong format passport")
#
#
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError(f"Seria an number passport must be a int")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.__old = old
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#     @property
#     def passport(self):
#         return self.__passport
#
#     @passport.setter
#     def passport(self, ps):
#         self.verify_ps(ps)
#         self.__passport = ps
# p1 = Person('Балашин Сергей Михайлович', 30, '1234 567890', 80.0)
# # p2 = Person('Балашин Сергей Михайлович', 30, '1234 567890', 80.0)
#
# p1.old = 100
# p1.passport = '1231 123123'
# p1.weight = 70.0
# print(p1.__dict__)

# class Square:
#     def __init__(self, s):
#         self.side = s
#
#     # @property
#     def area(self):
#         return self.side ** 2
#
# s1 = Square(3)
# print(s1.side)s
# print(s1.area)


# class Square:
#     s_list = []
#     def __init__(self):
#         # self.side = s
#         self._voltage = 10000
#     @property
#     def lists(self, elt):
#         self.s_list = self.s_list.append(elt)
#
#     @property
#     def voltage(self):
#         return self._voltage
#     @voltage.setter
#     def voltage(self, value):
#         self._voltage = value
#
# s = Square()
# # print(s.side)
# s.voltage = 123123123
# print(s.voltage)
# Square.lists = 123
# print(Square.s_list)

text_1= "the-stealth-warrior"
text_2 = "ThE_STealth_Warrior"
def to_camel_case(text):
    str = text
    str = str.replace('-', '').replace('_', '')
    return str

print(to_camel_case(text_2))




