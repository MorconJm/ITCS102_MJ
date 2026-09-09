#conditional statement
import getpass

#conditional statement

username = 'sisig'
password = 'sisig123'

u = input("Enter your username--->")
p = getpass.getpass("Enter your password--->")

if username == u and password == p :
       print("ACCESS GRANTED")
else:
    print("ACESS DENIED")