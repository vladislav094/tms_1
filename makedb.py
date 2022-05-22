from person import Person, Manager
bob = Person("Bob Smith")
sue = Person("Sue Jones", job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

import shelve
db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(f'Value 1 = {sue.lastName()}, Value 2 = {bob.lastName()}')
    sue.giveRaise(.10)
    # print(sue.pay)
    print(sue, bob)
    tom = Manager('Tom Jones', pay=50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)