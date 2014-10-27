import datetime

currentDate = datetime.date.today()
daysToComplete = 0
cWeeks = 0
cDays = 0

adate = input('Enter your project deadline in format MM/DD/CCYY: ')
pdeadline = datetime.datetime.strptime(adate, "%m/%d/%Y").date()

daysToComplete = pdeadline - currentDate
cDays = daysToComplete.days

print("There are %d days remaining until your project is due" %cDays)

cWeeks = daysToComplete.days / 7
cDays = daysToComplete.days % 7

print("There are %d weeks" %cWeeks + " and %d days remaining until your project is due." %cDays)


