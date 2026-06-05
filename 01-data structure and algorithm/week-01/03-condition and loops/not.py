username = "admin"
password = "1234"
blocked = False

if username == "admin" and password == "1234" and not blocked:
    print("Login Success")
else:
    print("Access Denied")

 ## another example

 a = True
 b = False

 print(a and b)   # False
 print(a or b)    # True
 print(not a)     # False
