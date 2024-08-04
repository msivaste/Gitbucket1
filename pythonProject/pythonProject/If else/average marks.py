Tam = int(input("Tamil: "))
Eng = int(input("English: "))
Mat = int(input("Maths: "))
Sci = int(input("Science: "))
Soc  = int(input("Social: "))
avg = (Tam+Eng+Mat+Sci+Soc)/5
if(avg>=35):
    print("You are good to go")
else:
    print("Special classes required")