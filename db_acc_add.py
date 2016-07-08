def p1(u_id, name, pas):
    import sqlite3 as lite

    acc_db = lite.connect('jackbot.db')
    target = "insert into accounts values(" + u_id + ",'" + name + "','" + pas + "')"
    target =  str(target)


    with acc_db:

        t1 = acc_db.cursor()
        t1.execute(target)


    return target

