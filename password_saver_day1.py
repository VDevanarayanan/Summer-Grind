class PasswordManager:
    def __init__(self):
        self.file = "password.txt"

    def save_password(self):
        site = input("Enter site: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        with open(self.file, "a")as f:
            f.write(f"{site}, {username}, {password}\n")
        print("Saved successfully\n")

    def view_password(self):
        try:
            with open(self.file, "r")as f:
                print(f.read())
        except FileNotFoundError:
            print("No files saved yet")

    def search(self):
        search_site = input("Enter site name: ")
        with open(self.file, "r")as f:
            for line in f:
                site, username, password = line.strip().split(",")
                if (site == search_site):
                    print(f"Username: {username}\nPassword: {password}")
                    return
        print("Not found\n")


pm = PasswordManager()
while True:
    print("1: Save\n")
    print("2: View\n")
    print("3: Search\n")
    print("4: Exit\n")
    choice = input("Enter choice: ")
    if (choice == "1"):
        pm.save_password()
    elif (choice == "2"):
        pm.view_password()
    elif (choice == "3"):
        pm.search()
    elif (choice == "4"):
        print("Exiting..\n")
        break
    else:
        print("Invalid Choice\n")
