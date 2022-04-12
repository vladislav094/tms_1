list_peoples = [165, 163, 161, 160, 157, 157, 155, 154]
x = 162

# def number(x, q):
#     for i, elt in enumerate(x):
#         if q > elt:
#             x.insert(i, q)
#             break
#         elif q > elt:
#             x.append(q)
#             break
#     print(x)
# number(list_peoples, x)

def number(q, w):
    for i, elt in enumerate(q):
        if w > elt:
            q.insert(i, w)
            break
        elif x < elt:
            q.append(w)
            break
    print(q)

number(list_peoples, x)