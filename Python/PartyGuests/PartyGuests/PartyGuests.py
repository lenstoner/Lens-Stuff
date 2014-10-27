guestNbr = 0
partyList = []
name = ' '

# Get the list of party goers
while name != 'x':
    name = input("Enter guest name.  Enter x to stop: ")

    if name != 'x':
        partyList.append(name)
        guestNbr += 1

partyList.sort()

if guestNbr > 0:
    print("The current guests coming to the party are: ")
    for partyList in partyList :
        print(partyList)