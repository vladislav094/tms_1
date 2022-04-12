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


print(sorted([(1, 'value'),(2, 'end')], key=lambda x: x[1]))

