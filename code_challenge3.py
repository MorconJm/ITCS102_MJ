#Global Freight Calculator

sendername = input("What is your name? ")
itemtype = input("What item did you buy? ")
is_Fragile = bool(input("Is the item fragile:"))
if is_Fragile == True:
	print("Handle with care.")
else:
	print("Not fragile.")

weight = float(input("What is the weight of the item (in kg)? "))
distance = float(input("How much distance (in km)? "))

#base cost
base_cost = weight * 2.50
base_cost2 = distance * 0.15
base_cost3 = base_cost + base_cost2

#total of international AND express
total_int = base_cost3 * 1.40
total_int2 = total_int + 50

#total of express or international shipping
total_or = base_cost3 * 1.20
total_or2 = total_or + 25

#oversized > 30kg and > 1000km
total_os = base_cost3 + 30

#standard rate
total_sr = base_cost3

#free shipping
free_ship = 0

is_express = bool(input("Will it travel by express?"))
if is_express == True:
	print("You have answered True. Please proceed.")
else:
	print("Okay.")

is_international = bool(input("Will it travel by international shipping?"))
if is_express == True and is_international == True:
	print("The total shipping would amount to:",total_int2)
elif is_express == True or is_international == True and weight > 20:
	print("The total shipping would amount to:",total_or2)
elif weight > 30 or distance > 1000:
	print("The package is oversized. The total shipping would amount to:",total_os)
elif weight <= 2.0 and distance <= 100 and is_express != True and is_international != True:
	print("The total shipping would amount to:",free_ship)
else:
	print("The total shipping would amount to:",base_cost3) #or total_sr
	
