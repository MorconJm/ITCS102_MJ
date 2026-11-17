loan = float(input("ENTER EVENT"))
year = int(input("ENTER YEARS TO PAY"))
month = year * 12
principal = loan/month
remain = loan
for x in range (1, month + 1):
    remain = principal
    loan_int = remain * 0.00256
    monthly_pay = loan_int + principal
    print(x,principal,loan_int,round(principal,2))
    