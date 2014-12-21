from Time import Time

myTime4=Time()
myTime4.set_time(8, 59, 45)
myTime4.print_time()

for i in range(20):
    myTime4.print_time()
    myTime4.tick()

