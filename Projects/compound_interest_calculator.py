"""
---------- Compound Interest Calculator ----------
This program will calculate interest after puting 
them in project (i.e. after investing money) in   
couple of years. We need the initial amount,      
intrest rate and time we calculate in. This is    
the formula:                                      
                                                  
Result = P * ( 1 + R/100 )^t                    
--------------------------------------------------
"""

print("Welcome to my life changing app!")

try:
    principal = int(input("Enter the principle amount: "))
    rate = int(input("Enter interest rate: "))
    time = int(input("Enter time in years: "))
except Exception:
    print("Error: Invalid Input!")

if principal<0 or rate<0 or time<0:
    print("Error: Inputs cannot be negative!")
else:
    res = principal * pow((1 + rate/100), time)
    print(f"Your money will be: {res}$.")
