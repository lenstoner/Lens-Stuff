counter = 1

while (counter >= 1):
    try:
        number = 2.0 **counter
        counter += 0.001
    except OverflowError as oe:
        print(oe)
        print("The current value is %d" % (number))
        break
    except KeyboardInterrupt as ki:
        print(ki)
        print("The current value is %d" % (number))
        break

