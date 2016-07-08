def p1():
    fo1 = open('email.txt', 'r+')
    fo1r = fo1.read()
    e_l = []
    for x in fo1r.split():
        e_l.extend(x.split())
    return e_l