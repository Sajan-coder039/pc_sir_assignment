# 1. Define a class Student with attributes name, roll_number, and marks.
# Implement a method display_info() that prints the details of the student.
# Create an instance of Student and call the display_info() method to display
# the student's details.

class Student:
  def __init__(self,name,roll_number,marks):
    self.name=name
    self.roll_number=roll_number
    self.marks=marks

  def display_info(self):
    print("Name = ",self.name)
    print("Rollno = ",self.roll_number)
    print("marks = ",self.marks)

stu=Student("kartik",39,972)
stu.display_info()

# output= Name =  kartik
#         Rollno =  39
#         marks =  972

# 2. Create a base class Animal with a method speak() that prints "Animal makes
# a sound". Derive a class Dog from Animal and override the speak() method
# to print "Dog barks". Instantiate the Dog class and call its speak() method.

class Animal:
  def speak(self):
    print("Animal makes a sound")

class Dog(Animal):
  def speak(self):
    print("Dog barks")

dog=Dog()
dog.speak()

# output = Dog barks

# 3. Define a class BankAccount with private attributes account_number and
# balance. Implement methods to deposit and withdraw money, ensuring that
# the balance cannot go below zero. Provide a method to get the account
# details. Test the class by performing deposit and withdrawal operations.

class BankAccount:
  def __init__(self,account_number,balance):
    self.account_number=account_number
    self.balance=balance

  def deposit(self,amount):
    self.balance+=amount
    print(f"{amount} has been added successfully !!")

  def withdraw(self,amount):
    if self.balance >= amount:
      self.balance-=amount
      print(f"{amount} has been successfully withdrawn !!")
    else:
      print("insufficient balance")
B1=BankAccount("129361294",16999)
B1.deposit(900)
B1.withdraw(263)

# output= 900 has been added successfully !!
#         263 has been successfully withdrawn !!

# 4. Create a base class Shape with a method area(). Derive two classes
# Rectangle and Circle from Shape. Implement the area() method in both
# derived classes. Instantiate Rectangle and Circle, and demonstrate
# polymorphism by calling their area() methods.
import math
class Shape:
  def area(self):
    print("Area is not  defined for this shape")

class Rectangle(Shape):
  def __init__(self,length,width):
    self.length=length
    self.width=width
  def area(self):
    return self.length * self.width

class Circle(Shape):
  def __init__(self,radius):
    self.radius=radius

  def area(self):
    return math.pi*(self.radius**2)

rec=Rectangle(23,45)
print(f"the area of rectangle={rec.area()}")
cir=Circle(7)
print(f"the area of circle= {cir.area()}")

# output=  the area of rectangle=1035
#          the area of circle= 153.93804002589985

# 5. Define a class Person with attributes name and age. Derive a class Employee
# from Person with additional attributes employee_id and salary. Implement a
# method display_employee() in Employee that prints all the details. Create an
# instance of Employee and display the information.

class Person:
  def __init__(self,name:str,age:int):
    self.name=name
    self.age=age

class Employee(Person):
  def __init__(self,name,age,employee_id,salary):
    super().__init__(name,age)
    self.employee_id=employee_id
    self.salary=salary

  def display_employee(self):
    print(f"Name = {self.name}\n\
          Age= {self.age}\n\
          employee_id= {self.employee_id}\n\
          Salary= {self.salary}"
    )

employ=Employee("kartik",39,8271,1000)
employ.display_employee()

# output=   Name = kartik
#           Age= 39
#           employee_id= 8271
#           Salary= 1000

# 6. Define a class Vector with attributes x and y. Overload the + operator to add
# two Vector objects. Implement the __add__() method and test it by adding
# two Vector instances.

class  Vector:
  def __init__(self,x,y):
    self.x=x
    self.y=y

  def __add__(self,other):
    if isinstance(other,Vector):
      new_x=self.x + other.x
      new_y=self.y + other.y
      return Vector(new_x,new_y)

  def __str__(self):
    return f"the added vector is {self.x}i + {self.y}j"

v1=Vector(2,4)
v2=Vector(3,5)
print(v1+v2)

# output= the added vector is 5i + 9j

# 7. Create a class Book with attributes title and author. Overload the __str__()
# method to return a string representation of the Book object in the format
# "Title by Author". Test this method by printing a Book instance.

class Book:
  def __init__(self,title,author):
    self.title=title
    self.author=author

  def __str__(self):
    return f"{self.title} by {self.author}"
book = Book("The Dark Knight", "Kartik")
print(book)

# output= the dark knight by Kartik

# 8. Define a class Time with attributes hours, minutes, and seconds. Overload
# the == operator to compare two Time objects for equality. Implement the
# __eq__() method and test it by comparing two Time instances.

class Time:
  def __init__(self,hours,minutes,seconds):
    self.hours=hours
    self.minutes=minutes
    self.seconds=seconds

  def __eq__(self,other):
    if isinstance(other, Time):
      return self.hours==other.hours and self.minutes==other.minutes and self.seconds==other.seconds

    return f"get not a class object"

t1=Time(23,23,23)
t2=Time(23,23,23)
t3=Time(10,27,39)
print(t1==t2)
print(t1==t3)

# output= True
#         False

# 9. Define a class Person with attributes name and age. Define another class
# Address with attributes street, city, and zipcode. Create a Contact class that
# contains an instance of Person and Address. Implement methods to display
# the contact details. Create a Contact object and display its information.

class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age

class Address():
  def __init__(self,street,city,zipcode):
    self.street=street
    self.city=city
    self.zipcode=zipcode

class Contact:
    def __init__(self, person, address):
        self.person = person
        self.address = address

    def display(self):
        print(f"Name: {self.person.name}")
        print(f"Age: {self.person.age}")
        print(f"Street: {self.address.street}")
        print(f"City: {self.address.city}")
        print(f"Zipcode: {self.address.zipcode}")

person = Person("Kartik", 39)
address = Address("Naraephat", "Kathmandu", 44600)
contact = Contact(person, address)

contact.display()

# output= Name: Kartik
#         Age: 39
#         Street: Naraephat
#         City: Kathmandu
#         Zipcode: 44600