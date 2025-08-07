# 1. Write a Python function named greet_user that takes a user's name and prints:
def greet_user(name):
  print(f"Hello, {name}")
greet_user("sajan")

# 2. Hello, <name>! Welcome to Python. Call the function with a sample name.
def greet(name):
  print(f"Hello, {name}! Welcome to Python.")
greet("kartik")

# 3. Create a function power(base, exponent=2) that returns the result of base raised to the power of
# exponent.Demonstrate it with and without the exponent argument.
def power(base,exponent=2):
  return base**exponent

print(power(2,4))
print(power(3))

# 4. Write a function book_info(title, author, year) that prints book details.Call the function using
# keyword arguments in different orders.
def book_info(title, author, year):
  print(f"'{title}' by {author}, published in {year}.")
book_info("demon_slayer","japanese",2018)
book_info(year=2009,title="attack_on_titan",author="Hajime Isayama")

# 5. Create a function sum_numbers(*args) that accepts any number of numeric arguments and returns
# their sum.Test it with 2, 3, and 5 numbers.
def sum_numbers(*args):
  sum=0
  for i in args:
    sum+=i
  return sum
print(sum_numbers(2,3,5))

# 6. Write a function student_profile(**kwargs) that prints the key-value pairs passed (e.g., name, age,
# grade). Call it with at least three named arguments.
def student_profile(**kwargs):
  for key,value in kwargs.items():
    print(f"{key} : {value}")
student_profile(name="Kartik Sah", age=18, grade="A")

# 7. Write a lambda function to compute the square of a number.Use it to compute the square of 5 and
# 12.
square=lambda x : x**2
print(square(5))
print(square(12))

# 8. Given a list of numbers [1, 2, 3, 4, 5], use map() and a lambda function to return a new list with
# each number doubled.
lst=[1, 2, 3, 4, 5]
doubles=list(map(lambda x : 2*x,lst))
print(doubles)

# 9. Given a list [10, 15, 20, 25, 30], use filter() and a lambda function to extract numbers divisible by 10.
lst_=[10, 15, 20, 25, 30]
div=list(filter(lambda x:x%10==0,lst_))
div

# 10. Given a list of temperatures in Celsius [36.5, 37.0, 39.2, 35.6, 38.7],convert them to Fahrenheit
# using map(),Filter out those above 100°F using filter().
temp_cel=[36.5, 37.0, 39.2, 35.6, 38.7]

temp_frah=list(map(lambda x:round((x*(9/5))+32,2),temp_cel))

filter_temp=list(filter(lambda x:x>100,temp_frah))

print(filter_temp)


# Mini Project:
# Simple To-Do Manager Using Functional Programming
# Objective: Manage a list of to-do tasks using functions, lambda, filter, and map.
# Requirements:
# ● Allow adding tasks using a function add_task(task_list, task_name).
# ● Each task is a dictionary: { "name": str, "completed": bool }.
# ● Use lambda and filter() to list only incomplete tasks.
# ● Use map() to mark all tasks as completed.
# ● Include a search_tasks(task_list, keyword) function using filter() and lambda.
# Sample Workflow:
# tasks = []
# tasks = add_task(tasks, "Buy groceries")
# tasks = add_task(tasks, "Finish assignment")
# tasks = add_task(tasks, "Call friend")
# # List incomplete tasks
# print("Pending Tasks:", list_pending(tasks))

# # Mark all tasks as complete
# tasks = complete_all(tasks)
# # Search tasks with keyword "call"
# print("Search Result:", search_tasks(tasks, "call"))




def add_task(task_list, task_name):
  task={"name":task_name,"completed":False}
  task_list.append(task)
  return task_list

def list_pending(tasks):
  return list(filter(lambda task:not task["completed"],tasks))

def complete_all(tasks):
  return list(map(lambda task:{**task,"completed":True},tasks))

def search_tasks(tasks, word):
  return list(filter(lambda task:word.lower() in task["name"].lower(),tasks))

print('*'*20)
print("Simple To-Do Manager")
print('*'*20)
tasks=[]
tasks = add_task(tasks, "Buy groceries")
tasks = add_task(tasks, "Finish assignment")
tasks = add_task(tasks, "Call friend")
print("Pending Tasks:", list_pending(tasks))
tasks = complete_all(tasks)
print("Search Result:", search_tasks(tasks, "call"))