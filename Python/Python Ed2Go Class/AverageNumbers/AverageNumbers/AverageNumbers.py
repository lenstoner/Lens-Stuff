entries  = 0
endProcess = -1
value = 0
totalAmt = 0
AverageAmt = 0.0

while value != endProcess :
    value = eval(input("Enter a value. Enter -1 to end: "))

    if value == endProcess :
        continue

    totalAmt += value
    entries += 1

if entries > 0 :
    AverageAmt = totalAmt / entries
    print("The sum of your values is %d. The average of your values is %d."  %(totalAmt, AverageAmt))

else :
    print("You did not enter any values.")
