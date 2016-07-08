def p1():
    import name_reader
    n_l = []
    n_l.extend(name_reader.p1())
    return n_l

def p2():
    import re
    x = "zed"
    while x == "zed":
        n_c = p1()
        t1 = raw_input("What is your name?" + '\n')
        x = "zed"
        t1 = t1.lower()
        if t1 in n_c:
            x = "zed"
            print "please try another name."
        elif not re.match("^[a-z]*$", t1):
            x = "zed"
            print "please try another name"
        elif len(t1) > 15:
            x = "zed"
            print "please try another name"
        else:
            n_c.extend(t1.split())
            break
    return t1