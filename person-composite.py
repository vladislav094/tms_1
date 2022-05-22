class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return f"[Person: {self.name}, {self.job}, {self.pay}]"

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)

    def __repr__(self):
        return str(self.person)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=500)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(f'Value 1 = {sue.lastName()}, Value 2 = {bob.lastName()}')
    sue.giveRaise(10)
    print(sue.pay)
    print(sue, bob)
    mat = Manager('Mat Damion', pay=50000);
    mat.giveRaise(.10)
    print(mat.lastName())
    print(mat)
    print(f"--All three--")
    for obj in (bob, sue, mat):
        obj.giveRaise(.10)
        print(obj)