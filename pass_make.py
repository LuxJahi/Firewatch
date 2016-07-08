import re

def p1():
    x = 1
    while x == 1:
        t1 = raw_input("please enter a password \n")
        if not re.match("^[a-z]*$", t1):
            x = 1
            print "please try again"
        elif len(t1) > 15 or len(t1) < 5:
            x = 1
            print "please try again!"
        else:
            break
            x = 0
    return t1