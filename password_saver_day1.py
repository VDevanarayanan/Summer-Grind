while True:
    print("Choice 1: Save a password\n")
    print("Choice 2: View Saved passwords\n")
    print("Choice 3: Exit\n")
    choice = input("Enter choice")
    if choice == "1":
        site = input("Enter site:  ")
        username = input("Enter username:  ")
        password = input("Enter password:  ")
        with open("password.txt", "a") as f:
            f.write(f"{site},{username},{password}\n")
        print("Saved successfully\n")
    elif choice == "2":
        with open("password.txt", "r")as f:
            print("Saved passwords\n")
            print(f.read())
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
