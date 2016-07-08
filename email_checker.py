def p1():
    import email_reader
    e_l = []
    e_l.extend(email_reader.p1())
    return e_l

def p2():
    import re
    x = "zed"
    while x == "zed":
        e_c = p1()
        t1 = raw_input("What's your email address?" + '\n')
        x = "zed"
        t1 = t1.lower()
        if t1 in e_c:
            x = "zed"
            print "please try another name."
        else:
            e_c.extend(t1.split())
            break
    return t1