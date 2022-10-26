#Roan Mason
#May 3, 2021
#Ask the user to enter a username and a password.  If the credentials are acceptable to you (you can make up any username/password combo you want), display the message “ACCESS GRANTED”. Otherwise, display the message “ACCESS DENIED”.

#ask for username
username = input("Username: ")
password = input("Password: ")

#if the username and password is correct it says so. if not it says its not correct
if username == "Mason" and password == "admin":
        print("ACCESS GRANTED")
else:
        print("ACCESS DENIED")