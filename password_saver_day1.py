site = input("Enter site: ")
username = input("Enter username: ")
password = input("Enter password: ")
with open("passwords.txt", "a") as f:
    f.write(f"{site},{username},{password}\n")
print("Saved successfully")

choice = input("Do you wish to see saved passwords(yes/no): ")
if choice == "yes":
    with open("passwords.txt", "r") as f:
        print("\nSaved passwords\n")
        print(f.read())
