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


# Project 2
# Create a simple banking system that:
# ● Stores customer info in a file
# ● Allows deposits and withdrawals using functions
# ● Updates customer balance
# ● Logs all transactions in a separate file
# ● Handles exceptions gracefully
# Files Used:
# customers.txt — stores customer records in the format:
# name,accountnumber,balance
# transactions.txt — appends every deposit or withdrawal record with timestamp

import os
from datetime import datetime

def add_account():
    global name,accountnumber,balance
    name=input("enter the name: ").capitalize()       
    accountnumber=int(input("enter the account holder: "))
    balance=float(input("enter the current balance: "))
    try:
        with open("customers.txt","w") as file:
            file.writelines(str({"name " : name,"Account Number ":accountnumber,"balance ":balance}))
    except Exception as ex:
        print("there is an error ",ex)


def deposit(amount):
    try:
        with open("customers.txt","w") as file:
            content=file.write(str({"name " :name,"Account Number ":accountnumber,"balance ":(balance+amount)}))
    except Exception as ex:
        print("there is an error ",ex)


def withdraw(amount):
    if balance>amount:
        try:
            with open("customers.txt","w") as file:
                content=file.write(str({"name " :name,"Account Number ":accountnumber,"balance ":(balance-amount)}))
        except Exception as ex:
            print("there is an error ",ex)
    else:
        print("insufficent money ! ")

def transactions(context):
    try:
        with open("transactions.txt","a") as file:
            file.write(context + "\n")
    except Exception as ex:
        print("there is an error",ex)

while True:
    print("!!!!!! simple banking system !!!!!!\n")
    print("1.for new account: ")
    print("2.deposit money ")
    print("3.withdraw money ")
    print("4. Exit ")

    choice=int(input("\nEnter choice number: "))
    if choice==1:
        add_account()

    elif choice==2:
        now=datetime.now()
        amount=float(input("enter the amount: "))
        deposit(amount)
        transactions(f"{amount} has been deposited at {now}")

    elif choice==3:
        now=datetime.now()
        amount=float(input("enter the amount: "))
        withdraw(amount)
        transactions(f"{amount} has been withdrawn at {now}")

    elif choice==4:
        break
    else:
        print("invalid choice !!!")