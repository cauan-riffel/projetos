def marge_list(l1, l2):
    l3 = []
    for i in l1:
        if not i in l3:
            l3.append(i)
    for i in l2:
        if not i in l3:
            l3.append(i)
    l3.sort()
    return l3


print(marge_list([1, 4, 2, 6, 8, 5, 2, 6, 9, 0, 3, 1, 3],
      [1, 2, 4, 7, 4, 2, 5, 8, 9, 6, 3, 1, 3, 6, 8]))
