import os

FILENAME = "contacts.txt"

def load_contacts():
    contacts = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    return contacts

def save_contacts(contacts):
    with open(FILENAME, "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")

def main():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Show All")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            contacts[name] = phone
            save_contacts(contacts)
        elif choice == "2":
            name = input("Search name: ")
            print("Phone:", contacts.get(name, "Not found"))
        elif choice == "3":
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        elif choice == "4":
            name = input("Name to delete: ")
            if name in contacts:
                del contacts[name]
                save_contacts(contacts)
                print("Deleted.")
            else:
                print("Not found.")
        elif choice == "5":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
