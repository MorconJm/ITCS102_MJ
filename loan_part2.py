loan = float(input("ENTER LOAN AMOUNT"))
year = int(input("ENTER YEARS TO PAY"))
month = year * 12

remain = loan
principal = loan / month

#for loop
print("|MONTH\t|\tPAYMENT\t\t|\tINTEREST\t|\tPRINCIPAL\t|\tBALANCE\t|")
for count in range(1, month + 1):
    remain -= principal
    interest = remain * 0.00256
    pay = interest + principal
    print(f"|{count}\t|\t{round(pay,2)}\t\t|\t{round(interest,2)}\t\t|\t{round(principal,2)}\t|\t{round(remain,2)}\t|")
    