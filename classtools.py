class AttrDisplay:
    """
    Предоставляет наследуемый метод перегрузки отображения, который показывает
    экземпляры с их именами классов и пары имя=значение для каждого атрибута,
    сохраненного в самом экземпляре (но не атрибутов, унаследованных от его классов) .
    Может соединяться с любым классом и будет работать на любом экземпляре.
    """
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append(f" %s = %s" % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __repr__(self):
        return f"[%s:%s]" % (self.__class__.__name__, self.gatherAttrs())

if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2

        # def gatherAttrs(self):
        #     return f"Spam"

    class SubTest(TopTest):
        pass

# X = TopTest()
# Y = SubTest()
# print(X)
# print(Y)
# print(X.__class__.__dict__)
# print(TopTest.__bases__)
# print(dir(X))
