sGrades   = {}

grade = 0
name   = " "

while (grade != 999) :
    grade = int(input("Enter grade (999 to quit): "))

    if (grade == 999) :
        continue

    name = input("Enter student's name: ")
    sGrades[name] = grade

   
for current_key in sGrades.keys():
    print(current_key, "\t", sGrades[current_key])

while (name != "999") :
    name = input("Enter the student name to show their grade: ")
    
    if (name =="999") :
        continue

    if (name in sGrades) :
        print("The grade for ", name, " is ", sGrades[name])

    else :
        print(name, " is not a student")
