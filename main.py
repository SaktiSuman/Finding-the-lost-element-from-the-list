def lostElement(list1, list2):
    x = set(list1)
    y = set(list2)
    if len(x) > len(y):
        print(list(x - y))
    else:
        print(list(y - x))
list1 = [12, 23, 34, 45]
list2 = [12, 23, 34]
lostElement(list1, list2)