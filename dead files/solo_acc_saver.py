def p1(u_name, u_pass, u_id):
    u_id2 = str(u_id) + ".txt"
    fo1 = open(u_id2, "w+")
    fo1.write(u_name + "\n" + u_pass + "\n" + u_id)
    fo1.close()
    return "solo finished"