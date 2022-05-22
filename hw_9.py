# class Book:
#     book_list = []
#
#     def __init__(self, title, author, pages, isbn, reserve=False):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.isbn = isbn
#         self.reserve = reserve
#         Book.book_list.append(self)
# class User:
#     taken_books = []
#     reserved_book = []
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def take_book(self, Book):
#         if Book in Book.book_list:
#             User.taken_books.append(Book)
#             Book.book_list.remove(Book)
#             print(f"Вы взяли книгу '{Book.title}'")
#         elif Book not in Book.book_list:
#             print(f"Книгу '{Book.title}'уже кто-то читает.")
#
#     def return_book(self, Book):
#         if Book in User.taken_books:
#             Book.book_list.append(Book)
#             User.taken_books.remove(Book)
#             print(f"Вы вернули книгу '{Book.title}'")
#         elif Book not in User.reserved_book:
#             print(f"Вы уже возвращали книгу '{Book.title}'")
#
#
#
# b1 = Book('Harry Potter', 'J.Roling', 654, 172345)
# b2 = Book('War and peace tom 1', 'L.Tolstoy', 927, 23456)
# u1 = User('Ivan', 23)
# u2 = User('Sergey', 17)
# print(b1.__dict__)
# print(b2.__dict__)
# print(Book.book_list)
# u1.take_book(b1)
# u2.take_book(b1)
# u1.return_book(b1)
# u1.return_book(b1)
import datetime
from datetime import date
import arrow
"""Создайте класс инвестиция. Который содержит необходимые поля и методы, например
сумма инвестиция и его срок.
Пользователь делает инвестиция в размере N рублей сроком на R лет под 10% годовых
(инвестиция с возможностью ежемесячной капитализации - это означает, что проценты
прибавляются к сумме инвестиции ежемесячно).
Написать класс Bank, метод deposit принимает аргументы N и R, и возвращает сумму,
которая будет на счету пользователя."""
a = arrow.get('2017-05-21')
b = arrow.get('2018-01-01')
delta = b - a
print(delta)

class Bank:
    list_of_amount_investment = {}
    def __init__(self, amount, period_year=None, period_month=None):
        """
        :param amount: Сумма вклада
        :param period_year: Период лет
        :param period_month: Период месяцев
        """
        self.amount = amount
        self.period_year = period_year
        self.period_month = period_month

    def deposit_for_year(self):
        for elt in range(self.period_year):
            result = (self.amount * 10.0) * (self.period_year / 100.0)

        print(f'За указанный период сумма % по вкладу составит: {result}')
        print(f"Общая сумма вклада и % по вкладу составит: {self.amount + result}")
        return result

    # def deposit_for_month(self):
    """Эта функция требует доработки"""
    #     for elt in range(self.period_year):
    #         day_in_year = self.period_year * 365
    #     print(day_in_year)
    #     for elt in range(self.period_month):
    #         # result = self.period_month * 10
    #         result = self.amount * 10 * self.period_month / 100
    #     print(f'За указанный период сумма % по вкладу составит: {result}')
    #     print(f"Общая сумма вклада и % по вкладу составит: {self.amount + result}")
    #     return result
"""Функция leap_year и day_in_month написаны дл"""
# def leap_year(year):
#     if year % 400 == 0:
#         return True
#     if year % 100 == 0:
#         return False
#     if year % 4 == 0:
#         return True
#     return False

# def day_in_month(month, year):
#     if month in {1, 3, 5, 7, 8, 10, 12}:
#         return 31
#     if month == 2:
#         if leap_year(year):
#             return 29
#         return 28
#     return 30
# print(day_in_month(4, 2022))

b1 = Bank(1000, 12, 10)

b1.deposit_for_year()
b1.deposit_for_month()
# d1 = datetime.datetime.today()
#
# # d1 = d1 + datetime.date(year=3)
#
# print(datetime.datetime.now())
# print(d1)
# print(datetime.datetime.today())


# a = {'Tom': 1000, 'Brad': 1500, 'Jhon':500}
# print(a)
# a['Tom'] += 150
# print(a)