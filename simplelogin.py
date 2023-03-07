users = {"user1": "password1", "user2": "password2", "user3": "password3"}

def login():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in users and users[username] == password:
            print("Login successful!")
            break
        else:
            print("Invalid username or password. Try again.")

login()
