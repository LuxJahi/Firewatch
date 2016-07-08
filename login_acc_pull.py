def p1(y):
    f_n = y
    fo1 = open(f_n, "r")
    t1 = fo1.read()
    acc1 = []
    for x in t1.split():
        acc1.append(x)


    return acc1