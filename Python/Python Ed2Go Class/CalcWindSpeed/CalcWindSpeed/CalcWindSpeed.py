speed = eval(input("Enter the current wind speed: "))

if speed >= 74 and speed <= 95:
    category = 1
elif speed >= 96 and speed <= 110:
    category = 2
elif speed >= 111 and speed <= 130:
    category = 3
elif speed >= 131 and speed <= 155:
    category = 4
elif speed >= 156:
    category = 5
else:
    category = 0

if category > 0:
    print("This is a category %d storm with a wind speed of %d." % (category, speed))
else:
    print("This is a mild storm with a wind speed of %d." % speed)
