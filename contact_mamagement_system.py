import os

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name},{self.phone},{self.email}"

class ContactManager:
    filename = "contact.txt"

    @staticmethod
    def ensure_file_exists():
        """ Ensures that contact.txt exists before operations """
        if not os.path.exists(ContactManager.filename):
            with open(ContactManager.filename, 'w') as file:
                pass  # Creates an empty file

    @staticmethod
    def add_contact(contact):
        """ Adds a new contact and creates the file if it doesn't exist """
        ContactManager.ensure_file_exists()  # Ensures file exists
        with open(ContactManager.filename, 'a') as file:
            file.write(f"{contact.name},{contact.phone},{contact.email}\n")
        print("✅ Contact added successfully!")

    @staticmethod
    def search_contact(name):
        """ Searches for a contact """
        ContactManager.ensure_file_exists()
        with open(ContactManager.filename, 'r') as file:
            contacts = file.readlines()
            for contact in contacts:
                details = contact.strip().split(",")
                if details[0].lower() == name.lower():
                    return f"✅ Found: Name: {details[0]}, Phone: {details[1]}, Email: {details[2]}"
        return "❌ Contact not found"

    @staticmethod
    def modify_contact(name, new_phone, new_email):
        """ Modifies an existing contact """
        ContactManager.ensure_file_exists()
        contacts = []
        found = False

        with open(ContactManager.filename, 'r') as file:
            contacts = file.readlines()

        with open(ContactManager.filename, 'w') as file:
            for contact in contacts:
                details = contact.strip().split(",")
                if details[0].lower() == name.lower():
                    file.write(f"{name},{new_phone},{new_email}\n")  # Modify
                    found = True
                else:
                    file.write(contact)

        if found:
            print("✅ Contact modified successfully!")
        else:
            print("❌ Contact not found!")

    @staticmethod
    def delete_contact(name):
        """ Deletes a contact """
        ContactManager.ensure_file_exists()
        contacts = []
        found = False

        with open(ContactManager.filename, 'r') as file:
            contacts = file.readlines()

        with open(ContactManager.filename, 'w') as file:
            for contact in contacts:
                details = contact.strip().split(",")
                if details[0].lower() != name.lower():
                    file.write(contact)
                else:
                    found = True

        if found:
            print("✅ Contact deleted successfully!")
        else:
            print("❌ Contact not found!")

    @staticmethod
    def display_contacts():
        """ Displays all contacts """
        ContactManager.ensure_file_exists()
        with open(ContactManager.filename, 'r') as file:
            contacts = file.readlines()
            if not contacts:
                print("📂 No contacts found!")
                return
            print("\n📋 All Contacts:")
            for contact in contacts:
                details = contact.strip().split(",")
                print(f"👤 Name: {details[0]}, 📞 Phone: {details[1]}, 📧 Email: {details[2]}")
        print()

# Test the Contact Manager

# 1️⃣ Add a contact
contact1 = Contact("Jai Desai", "234567891", "jaidesai@gmail.com")
ContactManager.add_contact(contact1)

# 2️⃣ Display all contacts
ContactManager.display_contacts()

# 3️⃣ Search for a contact
print(ContactManager.search_contact("Jai Desai"))

# 4️⃣ Modify a contact
ContactManager.modify_contact("Jai Desai", "9999999999", "jai.new@gmail.com")
ContactManager.display_contacts()  # Show updated contacts

# 5️⃣ Delete a contact
ContactManager.delete_contact("Jai Desai")
ContactManager.display_contacts()  # Show contacts after deletion
