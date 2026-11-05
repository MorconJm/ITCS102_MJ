from getpass import getpass

isLogin = False
    
while isLogin == False:
    username = input("USERNAME")
    password = getpass ("PASSWORD")
    
    if username == "user1" and password == "sigma123":
        print("ACCESS GRANTED")
        isLogin = True
    else:
        print("ACCESS DENIED")
    