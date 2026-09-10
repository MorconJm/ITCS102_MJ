print("Hello, this is your divided deposits!")

money = 3800

libo = money //1000 #--> 3
libo_sukli = money % 1000
#print(libo_sukli)
#libo_sukli = money -(libo * 1000)

five_h = libo_sukli // 500
five_sukli = libo_sukli % 500

two_h = libo_sukli // 200
two_sukli = five_sukli % 200

print("1000 -",libo)
print("500-",five_h)
print("200 -",two_h)
print(two_sukli)