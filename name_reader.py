def p1():
    import sqlite3 as lite

    t1 = lite.connect('jackbot.db')
    count = 0
    n_l = []
    g1 = []

    with t1:
        t1.text_factory = str
        target = t1.cursor()
        target.execute("select user from accounts")


        while True:

            x = target.fetchone()

            if x == None:
                break

            g1.append(x[0])
            g2 = g1[count]
            n_l.append(g2.lower())
            count = count + 1

    return n_l
