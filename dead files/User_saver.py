import pickle

#===Dictionary titles==========
user_id_save = [0]
user_password_save = {0:'blah',}
user_name_save = {'zed': 000, }

#===Loading files============


#===account creation + account name check=========
print "Create new account"

def account_creation():
    User_name = raw_input("What Is Your Name? \n")


    if User_name in user_name_save:
        print "That name is taken. Please choose another."
        return "zxcw2"
    else:
        User_ID = len(user_id_save)
        user_id_save.append(User_ID)
        user_name_save.update({User_name : User_ID})
        u_p = account_password_creation()
        user_password_save.update({User_ID : u_p})

        fo1 = open(User_name, "a+")
        t2 = str(User_ID) + '\n' + str(User_name) + '\n' + str(u_p)
        fo1.write(t2)
        fo1.close()



def account_password_creation():

    User_password = raw_input("Please Enter Your Password \n")
    return User_password


#===Account creation fail checker =========
def fail_checker(x):
    if x == "zxcw2":
        account_creation()


#===Calling for functions ===============
t1 = account_creation()
fail_checker(t1)

########!!!!!!!!!!!######!!!!!!!######
#====printing section=========
print "=======displaying end product======"
for x in user_name_save:
    print x
    f1 = user_name_save.get(x)
    print user_password_save[f1]
    f2 = user_name_save.get(x)
    print user_id_save[f2]
#---------------------------------------------


#====opening files==============
usn = open("usn.txt", "a+")
ups = open("ups.txt", "a+")
uid = open("uid.txt", "a+")

#====writing to the file========
for x in user_name_save:
    usn.write(x + '\n')
    g1 = user_name_save.get(x)
    g2 = str(user_password_save[g1])
    ups.write(g2 + '\n')
    h1 = user_name_save.get(x)
    h2 = str(user_id_save[h1])
    uid.write(h2 + '\n')



#====closing files=========
usn.close()
ups.close()
uid.close()




