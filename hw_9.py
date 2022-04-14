class Book:
    book_list = []

    def __init__(self, title, author, pages, isbn, reserve=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserve = reserve
        Book.book_list.append(self)
class User:
    taken_books = []
    reserved_book = []
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def take_book(self, Book):
        if Book in Book.book_list:
            User.taken_books.append(Book)
            Book.book_list.remove(Book)
            print(f"Вы взяли книгу '{Book.title}'")
        elif Book not in Book.book_list:
            print(f"Книгу '{Book.title}'уже кто-то читает.")

    def return_book(self, Book):
        if Book in User.taken_books:
            Book.book_list.append(Book)
            User.taken_books.remove(Book)
            print(f"Вы вернули книгу '{Book.title}'")
        elif Book not in User.reserved_book:
            print(f"Вы уже возвращали книгу '{Book.title}'")



b1 = Book('Harry Potter', 'J.Roling', 654, 172345)
u1 = User('Ivan', 23)
u2 = User('Sergey', 17)

print(b1.__dict__)
u1.take_book(b1)
u2.take_book(b1)
u1.return_book(b1)
u1.return_book(b1)
