# Project 1
# Create a CLI (Command Line Interface) contact book that allows users to:
# ● Add a new contact (append to file)
# ● View all contacts (read from file)
# ● Search for a contact (read and filter)
# ● Handle file-related exceptions (e.g., file not found)
# File Used:
# contacts.txt (stores contact info: Name, Phone)

def add_contact():
    try:
        with open("contacts.txt","a") as file:
            content=input("enter the name to add: ")
            phone=int(input("enter the phone number: "))
            diction={"Name":content,"Phone":phone}        
            file.write(str(diction) + "\n")
            print("successfully added !!")
    except FileNotFoundError:
        print("!!! file not found !!")

def view_contact():
    try:
        with open("contacts.txt","r") as file:
            print(file.read())  
    except FileNotFoundError:
        print("!!! file not found !!")        

def search_contact(name):
    try:
        with open("contacts.txt","r")as file:
            content=file.readlines()
            return list(filter(lambda cont:name.lower() in cont.lower(),content))
        
    except FileNotFoundError:
        print("!!! file not found !!")
    
print(search_contact("kartik"))
def main():
    while True:
        print('*'*30)
        print("!!!! contact_book!!!!")
        print("1. Add new contact!")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")
        print('*'*30)
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            print(search_contact(input("enter the Name of contact: "))[0])
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()

