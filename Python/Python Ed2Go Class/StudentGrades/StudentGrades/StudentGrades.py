import shelve
import pickle


gradeFile = shelve.open('C:/PythonData/studentgrades.txt','c')

grade = 0
name   = " "

while (grade != 999) :
    try:
        grade = int(input("Enter grade (999 to quit): "))

    except ValueError:
        print("You must enter a number as a grade")
        continue

    if (grade == 999) :
        continue

    name = input("Enter student's name: ")
    gradeFile[name] = grade
    

gradeFile.sync()
 
for current_key in gradeFile.keys():
    print(current_key, "\t", gradeFile[current_key])


while (name != "999") :
    name = input("Enter the student name to show their grade: ")
    
    if (name =="999") :
        continue

    if (name in gradeFile) :
        print("The grade for ", name, " is ", gradeFile[name])

    else :
        print(name, " is not a student")

gradeFile.close()

