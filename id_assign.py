def p1():
    import sqlite3 as lite

    t1 = lite.connect('jackbot.db')
    with t1:
        target = t1.cursor()
        target.execute("select id from accounts")
        id_pull = target.fetchall()

    id_c = []
    for x in id_pull:
        id_c.append(x[0])



    id_a = len(id_c)
    x = "zed"
    while x == "zed":
        id_c_2 = []
        for z in id_c:
            y = int(z)
            id_c_2.append(y)


        if id_a in id_c_2:
            x = "zed"
            id_a = id_a + 1
        else:
            id_c.extend(str(id_a))
            x = "finished"



    return str(id_a)