import turtle


aNumberSides = input("How many sides: ")
numberSides = int(aNumberSides)

for firstcount in range(numberSides):
    turtle.forward(40)
    turtle.right(int(360/numberSides))

    for secCount in range(numberSides):
        turtle.forward(20)
        turtle.right(int(360/numberSides))

