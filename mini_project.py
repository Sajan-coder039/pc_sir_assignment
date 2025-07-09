# Design and implement a Student Report Card Management System using Python that
# allows a teacher to:

# ● Add new student records (name, roll number, subject-wise marks).
# ● View the report of all students.
# ● Display the topper(s) of the class based on average marks.
# ● Search for a student by roll number.
# ● Display all students who have failed in one or more subjects.
# ● Optionally update marks of any student.. 
import pandas as pd
subject_lits=["English","Nepali","Math","Science","Social","Drawing"]
roll_number_list = ["082bel039", "082bel040", "082bel041", "082bel042"]
name_list = ["Sajan", "Kartik", "Arpan", "Sumit"]
subject_mark={
    "Sajan":{
        "English":87,
        "Nepali":80,
        "Math":96,
        "Science":91,
        "Social":92,
        "Drawing":87
    },
        "Kartik":{
        "English":44,
        "Nepali":84,
        "Math":90,
        "Science":81,
        "Social":72,
        "Drawing":77
    },
        "Arpan":{
        "English":40,
        "Nepali":70,
        "Math":86,
        "Science":71,
        "Social":72,
        "Drawing":77
    },
        "Sumit":{
        "English":67,
        "Nepali":60,
        "Math":66,
        "Science":61,
        "Social":62,
        "Drawing":67
    },
}

def add_student():       
    name=input("enter the student name -> ").capitalize()
    roll_no=input(f"enter {name}'s rollno like(081bel0XX)-> ")
    name_list.append(name)
    roll_number_list.append(roll_no)
    temp_dict={}
    for subject in subject_lits:
        mark=int(input(f"enter the {subject}'s mark: "))
        temp_dict[subject]=mark

    subject_mark[name]=temp_dict
    print(f"{name}'s record added successfully!\n")

def view_student():
    df=pd.DataFrame(subject_mark)
    print(df)
    
def topper_student():

    avg_dict={}
    for name,mark_dit in subject_mark.items():
        sum=0
        for sub,mark in mark_dit.items():
            sum+=mark
        avg=round(sum/6,2)
        avg_dict[name]=avg
    topper = max(avg_dict, key=avg_dict.get)
    print(f"{topper} has the highest average: {avg_dict[topper]}")
    
def search_student():
    roll_no=input(f"enter rollno like(082bel0XX) to find student-> ")
    if roll_no in roll_number_list:
        index=roll_number_list.index(roll_no)
        print(name_list[index])
        print('#'*30)

def fail_student():
    for name,mark_dit in subject_mark.items():
        for sub,mark in mark_dit.items():
            if mark<60:
                print(f"the student who has been failed {name}")
                break

def update_student():

    view_student()
    name=input("enter the student's name: ").capitalize()
    if name in subject_mark.keys():
        subject=input("enter the subject: ").capitalize()
        if subject in subject_mark[name].keys():
            subject_mark[name][subject]=int(input("enter the updated {subject}'s mark: "))
        


while True:
    print("\n===========================")
    print("  Student Record System")
    print("===========================\n")
    print("1. Add new student")
    print("2. View all student reports")
    print("3. Display topper(s)")
    print("4. Search by roll number")
    print("5. Show failed students")
    print("6. Update marks")
    print("7. Exit\n")

    choice = input("Enter your choice (1–7): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        topper_student()
    elif choice == "4":
        search_student()
    elif choice == "5":
        fail_student()
    elif choice == "6":
        update_student()
    elif choice == "7":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")