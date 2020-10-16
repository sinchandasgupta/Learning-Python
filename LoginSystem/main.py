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
        else:
            self.dict[user.name] = user.passwd
            f_handle = open("credentials.json", 'w')
            json.dump(self.dict, f_handle)
        f_handle.close()


print("Hey there!\n")

user = Person()

while True:
    user_type = input(
        "Enter Command: (Type 'help' to know the commands)\n> ").lower()
    if user_type == "new":
        while True:
            user.name = input("Type the username you want: ")
            try:
                f_handle = open("credentials.json", "r")
                credentials = json.load(f_handle)
                if user.name in credentials:
                    print("Sorry! This username is already taken...")
                    continue
                else:
                    break
            except:
                break
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
    elif user_type == "login":
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
    elif user_type == "help":
        print('''
help - Get help
new - Make a new account
login - Login to your existing account
quit - quit this program\n'''
              )
    elif user_type == "quit":
        quit()
    else:
        print("Enter a proper command\n")
