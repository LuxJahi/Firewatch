#import section
import login_user_name_checker
import password_check

#creating account space
acc = []

#login
acc = login_user_name_checker.p2()

#sesperating account info
a = acc[0]
b = acc[1]
c = acc[2]

#checking password
count = 0
t1 = password_check.p1(b)
print t1
while t1 == "You fail!" and count < 2:

    t1 = password_check.p1(b)
    count = count + 1

if t1 == "You fail!":
    print "Please start over"
    exit()

print "new system is a go"
print acc