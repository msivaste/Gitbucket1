Sal = int(input("Enter your monthly salary: "))
age = int(input("Age: "))
if(Sal>=20000) or (age<=25):
    Loan_amt = int(input("Enter required loan amount: "))
    if(Loan_amt<=50000):
        print("You are eligible for loan")
    else:
        print("Your maximum eligible loan amount is 50000")
else:
    print("Sorry! You are not eligible for loan")