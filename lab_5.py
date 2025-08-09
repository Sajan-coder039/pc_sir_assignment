# 1. Create a class Book with attributes title, author, and price. Write a
# constructor to initialize these values and create an object with sample data.
# ● Add a method display_info() to the Book class that prints the book's
# title, author, and price. Call this method using a Book object.
# ● Add a method update_price(new_price) to the Book class that updates
# the book's price. Demonstrate how to use it with an object.

class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    
    def display_info(self):
        return f"'{self.title}' by {self.author},\n cost: {self.price}."
    def update_price(self,new_price):
        self.price=new_price

bk=Book("life of genz","kartik",200)
bk.update_price(999)
print(bk.display_info())


# 2. Create a class Student with attributes name and marks. Create three objects
# of the class and display their details using a method show_details().

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def show_details(self):
        return f"Name: {self.name}\nmark obtained: {self.marks}"

stu1=Student("kartik",200)
stu2=Student("manish",201)
stu3=Student("dhiraj",202)
print(stu1.show_details())
print(stu2.show_details())
print(stu3.show_details())

# 3. Create a class BankAccount with attributes account_holder,
# account_number, and balance.
# ● Add methods deposit(amount) and withdraw(amount) that update the
# balance.
# ● Add a method show_balance() that prints the current balance.
# ● Create an object and perform a deposit, a withdrawal, and show the
# balance.

class BankAccount:
    def __init__(self,account_holder,account_number,balance):
        self.account_holder=account_holder
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if self.balance>amount:
            self.balance-=amount
        else:
            print("insufficient balance!!")

    def show_balance(self):
        return f"the current balance: {self.balance}"

ba=BankAccount("kartik",30975401343,1000)
ba.deposit(500)
ba.withdraw(1000)
print(ba.show_balance())