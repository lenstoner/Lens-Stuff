import csv
import sys

# Create variables for file and access method.
# fileName = "BDList.csv"
accessMode = "a"
bRecord = " "
bName = " "
bAge = " "
fileClosed = True

def writeToFile(recorddata, filename, fileClosed) :
    if (fileClosed) :
        myFile = open(filename, accessMode)
        
    if (recorddata != " ") :
        myFile.write(recorddata)
    else :
        myFile.close()

    return


# Open file for input.
# myFile = open(fileName, accessMode)

# Get name of file from user.
fileName = input("Please enter the file holding birthday data: ")

# Check the existence of the file.
accessMode = "r"
try :
    myFile = open(fileName, accessMode)
    myFile.close()
    accessMode = "a"

except FileNotFoundError :
    print("File " + fileName + " does not exist.")
    sys.exit()

while (bName != "x") :
    bName = input("Enter Name: ")

    if (bName != "x") :
        bAge = input("Enter Age: ")
        bRecord = '"' + bName + '"' + ',' + bAge + "\n"
        #myFile.write(bRecord)
        writeToFile(bRecord,fileName,fileClosed)
        fileClosed = True
    else :
        bRecord = " "
        writeToFile(bRecord, fileName, fileClosed)

# myFile.close()

# Display file contents
accessMode = "r"
with open(fileName, accessMode) as bdFile :

    # Read the file.
    fileData = csv.reader(bdFile)

    # Use join function to remove brackets and format the output.
    for row in fileData :
        print(', '.join(row))
 
