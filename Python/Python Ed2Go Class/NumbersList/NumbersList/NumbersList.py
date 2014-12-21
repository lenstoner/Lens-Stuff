vlist = []
index = 0
evalue = 0
total = 0

while evalue != -999 :
    evalue = int(input("Please enter a number (-999 exits): "))
    if evalue == -999 :
        continue
    vlist.append(evalue)
    index += 1

if index > 0 :
    for x in range(0,len(vlist)) :
        total += vlist[x]

    print("For this list of numbers:\n")
    print(vlist)
    print("\n\nThe average is %d" % (total / len(vlist)) )


