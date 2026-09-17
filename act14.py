#age(integers)
#is_employed(bool)
#credit_score(integer)
#annual_income(float)
#has_collateral(boolean) 

age = int(input("Are you 18?"))
is_employed = bool(input("Are you employed?"))
credit_score = int(input("ENTER CREDIT SCORE:"))
annual_income = float(input("ENTER INCOME:"))
has_collateral = bool(input("Do you have collateral? (True/False)"))

if age >= 18 and is_employed == True:
    print("PLEASE PROCEED")
else:
    print("ERROR")
# Base interest rate: 5.0%
print("tier 1")

if credit_score >= 750: 
  print("TIER 1")
elif annual_income >= 100000:
  base_rate1 = 4.5%
  print("your base rate is",base_rate)
else:
    base_rate1 = 5.0
    print("Base rate is",base_rate)

if 600 <= credit_score < 750:
 print("TIER 2")
elif annual_income < 40,000
base_rate2 = 9.5%
print("your base rate is",base_rate2)

else:
base_rate2 = 8.0
print("your rate is",base_rate2")
      
if has_collateral == True and base_rate2 == False
base= base_rate2 - 7.0
      print("Base rate is now",base)
      else:
      print("Yep")

if credit_score < 600 == True
print("ACCEPTED")
else:
 print("REGECTED")



