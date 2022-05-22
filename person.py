from classtools import AttrDisplay

"""
Регистрирует и обрабатывает сведения о людях.
Для тестирования классов из этого файла запустите его напрямую.
"""

class Person(AttrDisplay):
    """
    Регистрирует и обрабатывает сведения о людях.
    Для тестирования классов из этого файла запустите его напрямую.
    """
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    # def __repr__(self):
    #     return f"[Person: {self.name},{self.pay}]"

class Manager(Person):
    """
    Настроенная версия Person со специальными требованиями
    """
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        self.pay = int(self.pay * (1 + percent + bonus))

    def someThingElse(self):
        pass


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
    # print(f"--All three--")
    # for obj in (bob, sue, tom):
    #     obj.giveRaise(.10)
    #     print(obj)
    # print(bob.__class__, tom.__class__, sue.__dict__)