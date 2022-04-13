# s = lambda a, b: a + b
# print(s(2, 4))
# list = [5, 3, 0, -6, 8, 10, 1]
# def get_filter(a, filter=None):
#     if filter is None:
#         return a
#     res = []
#     for x in a:
#         if filter(x):
#             res.append(x)
#     return res


# r = get_filter(list, lambda x: x % 2== 0)
# print(r)


# print(sorted([(1, 'value'),(2, 'end')], key=lambda x: x[1]))


class Shop:

    all_products = []
    all_prices = []

    def __init__(self, title):
        self.title = title
        self._price = 0
        self.all_products.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
        self.all_prices.append(value)

    @classmethod
    def sum_overall_price(cls):
        overall_price = sum(cls.all_prices)
        return overall_price
    

google_pixel_5 = Shop('Google Pixel 5')
google_pixel_5.price = 500

google_pixel_6 = Shop('Google Pixel 6')
google_pixel_6.price = 1000

google_pixel_7 = Shop('Google Pixel 7')
google_pixel_7.price = 250

# google_pixel_5 = Shop('Google Pixel 5')
google_pixel_5.price = 123

print(Shop.sum_overall_price())