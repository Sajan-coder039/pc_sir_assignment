# 1. Write a program to input n numbers and store them in a list. Then perform the following
# operations: i) Using built in functions ii) without using built-in functions:
# a. Find the maximum and minimum number
# b. Sort the list in ascending order
# c. Remove duplicate elements

#source code
#i)
import random
lst=[random.randint(1,101) for _ in range(0,50)]
#a
max=max(lst)
min=min(lst)
print(f"maximum number={max}\nminimum number={min}")
#b
sortt=sorted(lst)
print(f"the sorted list is {sortt}")
#c
sett=set(lst)
remove=list(sett)
print(f"the remove duplicate list is {remove}")

#ii)
#a)
print(lst)
temp=0
for i in lst:
    if i>temp:
        temp=i
print(f"maximum is {temp}")
for i in lst:
    if i<temp:
        temp=i
print(f"minimum is {temp}")

#b)
new_list=[]
for_srt=lst
while for_srt:
    num=for_srt[0]
    for i in for_srt:
        if i<num:
            num=i
    new_list.append(num)
    for_srt.remove(num)
print(new_list)

#c)
remove_list=[]
temp_list=lst
for i in temp_list:
    if i not in remove_list:
        remove_list.append(i)

print(remove_list)
print(len(remove_list))

###############################################

# 2. Given two lists of integers, write a program to merge them into a single list and then
# remove the elements that are common in both.
import random
final_list=[]
lst1=[random.randint(0,10) for _ in range(0,12)]
lst2=[random.randint(0,10) for _ in range(0,12)]
print(f"{lst1}\n{lst2}")
mer_lst=lst1+lst2
common=list(set(lst1) & set(lst2))
for i in mer_lst:
    if i not in common:
        final_list.append(i)

print(final_list)

###############################################

# 3. Create a program that reads a sentence from the user and stores each word as an
# element of a list. Then count the frequency of each word using only lists.
user=input("enter the sentence: ").lower()
word_list=user.split()
new_=[]
count_list=[]
for word in word_list:
    if word in new_:
        index=new_.index(word)
        count_list[index]+=1
    else:
        new_.append(word)

        count_list.append(1)

for i in range(0,len(new_)):
    print(f"{new_[i]}:{count_list[i]}")
    
###############################################

# 4. Write a program to simulate a basic stack and queue using a list. Provide options to
# push, pop (stack), enqueue, and dequeue (queue).

stack=[]
quere=[]

while True:
    print("\nMenu:")
    print("1. Push to Stack")
    print("2. Pop from Stack")
    print("3. Enqueue to Queue")
    print("4. Dequeue from Queue")
    print("5. Display Stack and Queue")
    print("6. Exit")
    choice = int(input("Enter your choice (1–6): "))
    if choice==1:
        thing=input("enter the iten to push onto stack: ")
        stack.append(thing)
        print(f"the item {thing} had been pushed to stack")
    elif choice==2:
        if stack:
            popped=stack.pop()
            print(f"{popped} has been pop from stack")
        else:
            print("stack is empty!!!!1")
    elif choice==3:
        thing=input("enter the iten to enquere onto quere: ")
        quere.append(thing)
        print(f"the item {thing} had been enquere to quere")
    elif choice==4:
        if quere:
            popped=quere.pop(0)
            print(f"{popped} has been dequere from quere")
        else:
            print("stack is empty!!!!1")
    elif choice==5:
        print(f"\ncurrent stack {stack[::-1]}")
        print(f"current quere {quere}")
    elif  choice==6:
        print("thenks for using!!!")
        print("existed program")
        break
    else:
        print("enter the valid option")
        
###############################################

# 5. Write a Python function that accepts a list and returns a new list containing only the
# elements at even indexes and those that are prime numbers.
import random

def prime_checker(n):
    if n>0:
        if n>2:
            for i in range(2,n):
                if n%i==0:
                    return False
            return True 
        elif n<2:
            return False
        else:
            return True
    else:
        print("please, enter the positive number")
def checker(acc_list:list)->list:
    
    even_list=[x for x in acc_list if acc_list.index(x)%2==0 and prime_checker(x)]
    return even_list
random.seed(123)
acc_list=[random.randint(0,20) for _ in range(0,20)]
print(acc_list)
print(checker(acc_list))

###############################################

# 6. Write a program to create a tuple of n numbers, then find:
# a. The average of the numbers
# b. The median
# c. The mode (without using libraries)
import random

n = int(input("enter n: "))
tupl = tuple(random.randint(0, 20) for _ in range(n))
#a)
average=sum(tupl)/choice
print(f"average={average}")
#b)
lsst=sorted(list(tupl))
print(lsst)
if n%2==0:
    median=lsst[n//2]
    print(f"median={median}")
else:
    median=(lsst[(n//2)+1]+lsst[(n//2)-1])/2
    print(f"median={median}")

#c)
dict_count={}
for i in lsst:
    if i in dict_count.keys():
        dict_count[i]+=1
    else:
        dict_count[i]=1
print(dict_count)
freq=list(dict_count.values())
print(max(freq))
modes = [key for key, value in dict_count.items() if value == max(freq)]
print("Mode(s):", modes)

###############################################

# 7. Write a program that receives a list of tuples representing (x, y) coordinates. Determine
# whether the points form a straight line.
points = [(1, 2), (2, 4), (3, 7), (4, 8)]
if len(points)<2:
    print("it is a straight line ")
else:
    x1,y1=points[0]
    x2,y2=points[1]
    for i in range(2,len(points)):
        x3,y3=points[i]
        if (y2-y1)*(x3-x2)!=(y3-y2)*(x2-x1):
            print("not a straight line")
            break

    else:
        print("Straight line")
        
###############################################

# 8. Write a program to input two sets of student roll numbers: one who play cricket and
# another who play football. Find:
# a. Students who play both sports
# b. Students who play only one sport
# c. Students who play neither (given a master list of all students)

cricket = set(input("Enter roll numbers of students who play Cricket (comma-separated): ").split(","))
football = set(input("Enter roll numbers of students who play Football (comma-separated): ").split(","))
all_students = set(input("Enter roll numbers of ALL students in the class (scomma-separated): ").split(","))
#a)
print(cricket & football)
#b)
print(cricket ^ football)
#c)
print(all_students-(cricket | football))

###############################################

# 9. Create a set of random numbers. Add more numbers until the set has 10 unique
# elements. Also, remove the smallest and largest element.
ran_set={1,2,3,4,5}
while len(ran_set)<10:
    ran_set.add(int(input("enter the number")))
print("samllest number=",min(ran_set))
print("largest number=",max(ran_set))

###############################################

# 10. Write a Python function that accepts a sentence and returns a set of all unique vowels
# used.
def vowel_checker(sente:str)->None:
    vowel=set("aeiou")
    
    used_vowel=set([char for char in sente if char in vowel])
    print("set of all vowel : ",used_vowel)

sente=input("enter the sentence: ").lower()
vowel_checker(sente)
###############################################

# 11. Given a list of numbers with duplicates, use a set to remove the duplicates. Then,
# convert it back to a sorted list and display the result.
import random

given_list=[random.randint(0,10) for _ in range(0,20)]
given_list=list(set(given_list))
print(sorted(given_list))

###############################################

# 12. Create a dictionary to store student names as keys and their scores in three subjects as
# values (in a list). Write functions to:
# a. Display the average marks of each student
# b. Find the topper
# c. Update the marks of a student
students = {
    "Alice": [85, 90, 78],
    "Bob": [70, 88, 92],
    "Charlie": [95, 87, 85],
    "Diana": [60, 75, 80]
}
#a)
def average(stud:dict)-> dict:
    new_dict_st={}
    for key,value in stud.items():
        menn=sum(value)/len(value)
        new_dict_st[key]=round(menn,2)
    return new_dict_st
print(average(students))
dict_average=average(students)
#b)
llist=dict_average.values()
topper=[key for key,value in dict_average.items() if max(llist)==value]
print(topper)
#c)
students["Bob"][0]=90
print(students)

###############################################

# 13. Write a program that reads a text and counts the frequency of each character (excluding
# spaces and special characters) using a dictionary.
strin='''Mount Everest is the highest mountain in the world, standing at 8,848.86 meters (29,031.7 feet) above sea level.
It is located in the Himalayas on the border between Nepal and the Tibet Autonomous Region of China.'''
count_dixtt={}

sttt=strin.split()

for word in sttt:
    for char in word:
        if char in count_dixtt:
            count_dixtt[char]+=1
        else:
            count_dixtt[char]=1

print(count_dixtt)

###############################################

# 14. Build a dictionary where the keys are product names and the values are their prices.
# Implement options to:
# a. Add a new product
# b. Update price of an existing product
# c. Find products within a given price range
products = {
    "Apple": 120,
    "Banana": 50,
    "Milk": 200,
    "Bread": 150,
    "Eggs": 300
}
#a)
products["pineapple"]=230
#b)
products['Banana']=129
#c)
lower=int(input("enter the lowerlimit of price: "))
upper=int(input("enter the upperlimit of price: "))
for key,value in products.items():
    if value<=upper and value>=lower:
        print(key)

#####################################################


