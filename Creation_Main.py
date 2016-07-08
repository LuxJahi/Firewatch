#====== imports sections
import db_acc_add
import id_assign
import name_checker
import pass_make

#===pulling user list
name_list = name_checker.p1()

#=== creating account

a = name_checker.p2()
b = pass_make.p1()
c = id_assign.p1()

print c
#===== saving account
db_acc_add.p1(c,a,b)