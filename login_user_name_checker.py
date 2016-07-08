def p1():
    import name_reader
    n_l = []
    n_l.extend(name_reader.p1())
    return n_l

def p2():
    un = raw_input("Please enter your user name: \n")
    un = un.lower()
    n_l = p1()
    #check for name in db first
    if un in n_l:
        #builds id database list
        import sqlite3 as lite
        t1 = lite.connect('jackbot.db')

        loc_id = "select id from accounts where user = '" + un +"'"
        loc_id = str(loc_id)
        loc_pass = "select password from accounts where user = '" + un +"'"
        loc_pass = str(loc_pass)
        uid_1 = []
        up_1 = []
        with t1:
            target = t1.cursor()
            target.execute(loc_id)
            id_list = target.fetchall()

        with t1:
            t1.text_factory = str
            target = t1.cursor()
            target.execute(loc_pass)
            pass_list = target.fetchone()

        for x in pass_list:
            up_1.append(x)
        for x in id_list:
            uid_1.append(x[0])

        r1 = []
        r1.append(un)
        r1.append(up_1[0])
        r1.append(uid_1[0])


        return r1


    #name was not found in db
    else:
        return "name not found"
