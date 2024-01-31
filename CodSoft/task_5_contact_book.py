class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        if name not in self.contacts:
            self.contacts[name] = {'Phone': phone_number, 'Email': email, 'Address': address}
            print(f"Contact {name} added successfully.")
        else:
            print("Contact with that name already exists. Use update option to modify.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for name, details in self.contacts.items():
                print(f"{name}: {details['Phone']}")

    def search_contact(self, keyword):
        found_contacts = []
        for name, details in self.contacts.items():
            if keyword.lower() in name.lower() or keyword in details['Phone']:
                found_contacts.append((name, details))
        return found_contacts

    def update_contact(self, name, phone_number, email, address):
        if name in self.contacts:
            self.contacts[name] = {'Phone': phone_number, 'Email': email, 'Address': address}
            print(f"Contact {name} updated successfully.")
        else:
            print("Contact not found. Use add option to create a new contact.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone_number, email, address)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contact(keyword)
            if found_contacts:
                print("Found Contacts:")
                for name, details in found_contacts:
                    print(f"{name}: {details}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            name = input("Enter name of the contact to update: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact_book.update_contact(name, phone_number, email, address)

        elif choice == '5':
            name = input("Enter name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
