import turtle

# Declare Variables
penColor = 'black'
lineLength = 0
angle = 0

# Get values from user
lineLength = int(input("Enter the line length.  Enter 0 to exit: "))
penColor = input("Which color? black, blue, red, or green: ")
angle = int(input("What angle? 0 - 360: "))

while lineLength != 0 :
    turtle.color(penColor)
    turtle.right(angle)
    turtle.forward(lineLength)

    lineLength = int(input("Enter the line length.  Enter 0 to exit: "))
    
    if lineLength != 0 :
        penColor = input("Which color? black, blue, red, or green: ")
        angle = int(input("What angle? 0 - 360: "))

print("You are an amazing artist!")