custCountry = ' '
custProvince = ' '
noTax = True

custCountry = input("What is your country?" )

if custCountry.lower() == "canada" :
    custProvince = input("What is your province? ")
    noTax = False

orderTotal = float(input("What is your order amount? "))

if noTax :
    taxAmount = 0
elif custProvince.lower() == "alberta" :
    taxAmount = orderTotal * 0.05
elif custProvince.lower() == "ontario" or custProvince.lower() == "new brunswick" \
     or custProvince.lower() == "nova scotia" :
         taxAmount = orderTotal * 0.13
else : 
    taxAmount = (orderTotal * 0.06) + (orderTotal * 0.05)

print("Total Order Amount:  $%.2f" %orderTotal)
print("Total Taxes ......:    %.2f" %taxAmount)
print("                     -----")
orderTotal += taxAmount
print("Total Purchase ...:   %.2f" %orderTotal)

