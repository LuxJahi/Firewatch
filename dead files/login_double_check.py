def p1(a,b,uid):
    import sqlite3 as lite

    t1 = lite.connect('jackbot.db')

    loc_id = "select id from accounts where user = '" + a + "'"
    loc_id = str(loc_id)
    loc_pass = "select password from accounts where user = '" + a + "'"
    loc_pass = str(loc_pass)
    uid_1 = []
    up_1 = []

    with t1:
        t1.text_factory = str
        target = t1.cursor()
        target.execute(loc_pass)

    uid

    acc = []
    name = a
    password = b
    for x in t1.split():
        acc.extend(t1.split())

    if name == acc[0]:
        if password == acc[1]:
            return 1
        else:
            return 2
    else:
        return 2



