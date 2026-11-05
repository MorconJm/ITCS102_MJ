isExpensive = True

while isExpensive == True:
    x = bool(input("IS GAS STILL EXPENSIVE?(TRUE/FALSE)"))

    if x == True:
        print("CONTINUING LOOP")
        continue
    else:
        break