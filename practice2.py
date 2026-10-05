age = int(input("Age --- "))
rev = float(input("Monthly Revenue --- "))
creditscore = int(input("Credit Score --- "))
years = float(input("Years in Business --- "))
defaults = bool(input("Defaults --- "))
collateralname = input("Collateral Name --- ")
collateralvalue = float(input("Collateral Value --- "))

max_loan = 0
base_fee = 0

if age >= 21 and defaults == False and years >= 2.0:
  print("Baseline passed.")
  if creditscore >= 720: #tier1
    max_loan = rev * 3
    print("The maximum loan is",max_loan)
    if rev >= 50000:
      base_fee = max_loan * 0.015
      print("The base fee rate is",base_fee)
    else:
      base_fee = max_loan * 0.025
      print("The base fee rate is",base_fee)
    if collateralvalue >= max_loan:
      print("Accepted.")
    else:
      print("Rejected: Insufficient collateral value for",collateralname)
    if collateralvalue % 5000 != 0:
      base_fee += 250
      print("An additional charge is added to your base fee:",base_fee)
    else:
      print("Collateral value divisible by 5000.")
  elif creditscore <= 620 and creditscore < 720: #tier2
    max_loan = rev * 1.5
    print("The maximum loan is",max_loan)
    if years >= 5.0:
      max_loan = rev * 0.02
      print("The maximum loan is",max_loan)
    else:
      max_loan = rev * 0.035
      print("The maximum loan is",max_loan)
  elif creditscore < 620: #tier3
    print("Rejected: Credit score below requirement.")
  else:
    print("Rejected: Credit score is low.")
else:
  print("Failed baseline.")