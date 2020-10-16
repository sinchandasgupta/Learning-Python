import json
import os


class Person(object):
    def __init__(self):
        self.name = ""
        self.passwd = ""
        self.dict = {}

    def writing(self):
        if os.path.exists("credentials.json"):
            f_handle = open("credentials.json", 'r')
            credentials = json.load(f_handle)
            credentials[user.name] = user.passwd
            os.remove("credentials.json")
            f_handle = open("credentials.json", 'w')
            json.dump(credentials, f_handle)
            f_handle.close()
        else:
            self.dict[user.name] = user.passwd
            f_handle = open("credentials.json", 'w')
            json.dump(self.dict, f_handle)
            f_handle.close()


print("Welcome to Blue-Leaf Software Solutions!\n")

user = Person()

while True:
    user_type = input("Enter user type (existing/new):\n> ")
    if user_type.lower() == "new":
        user.name = input("Type the username you want: ")
        while True:
            user.passwd = input("New Password: ")
            confirm_password = input("Confirm Password: ")
            if confirm_password == user.passwd:
                user.writing()
                print("You've successfully registered!\n")
                break
            else:
                print("Passwords do not match!")
                continue
    elif user_type.lower() == "existing":
        if os.path.exists("credentials.json"):
            f_handle = open("credentials.json", 'r')
            credentials = json.load(f_handle)
            while True:
                user.name = input("Enter your Username: ")
                if user.name in credentials:
                    while True:
                        user.passwd = input("Enter your password: ")
                        if user.passwd == credentials.get(user.name):
                            print("You have successfully logged in!")
                            quit()
                        else:
                            print("You've entered a wrong password")
                else:
                    print("Enter a correct username!")
                    continue
        else:
            print("There has not been any registrations!")
