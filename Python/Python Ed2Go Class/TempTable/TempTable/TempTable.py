cTemp = 0
fTemp = 0.0

def convertTemp (ctemp) :
    return ((9.0/5.0) * ctemp) + 32

print("****************************************************")
print("Celsius Temp\t\tFahrenheit Temp")

while cTemp <= 100 :
    fTemp = convertTemp(cTemp)
    print("%d\t\t\t%f" % (cTemp, fTemp))
    cTemp += 10

print("****************************************************")