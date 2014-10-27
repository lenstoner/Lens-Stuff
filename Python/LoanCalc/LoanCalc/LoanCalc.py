MonthlyPayment = 0
LoanAmount = 0
InterestRate = 0
NumberOfPayments = 0

nLoanAmount = input("What is the total loan amount? ")
LoanAmount = float(nLoanAmount)
nInterestRate = input("What is the interest rate?" )
InterestRate = float(nInterestRate)
nNumberOfPayments = input("How many monthly payments? ")
NumberOfPayments = float(nNumberOfPayments)

MonthlyPayment = (LoanAmount * InterestRate * (1 + InterestRate) * NumberOfPayments) \
                    / (((1 + InterestRate) * NumberOfPayments) - 1)
InterestRate = InterestRate * 100

print("\nFor a loan of $%.2f" % LoanAmount)
print(" with an interest rate of %.2f percent" % InterestRate)
print(" with %f payments" % NumberOfPayments)
print(" Your monthly payments are $%.2f." % MonthlyPayment)