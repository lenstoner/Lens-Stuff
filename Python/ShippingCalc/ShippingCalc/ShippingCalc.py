totalPurchase = 0
minAmount = 50
freeShipping = False
shipping = 10

totalPurchase = float(input("Enter the total purchase amount: "))

if totalPurchase >= minAmount :
    freeShipping = True
    shipping = 0

print("Purchases = $%.2f " %totalPurchase)
print("Shipping  =  %.2f " %shipping) 
totalPurchase += shipping
print("Total Due = $%.2f " %totalPurchase)
