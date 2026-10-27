n = int(input("INPUT SIZE OF X"))
for x in range(n):
    for y in range(n):
        if x + y == n-1 or  y==x:
            print("*", end=" ")
        else:
             print("", end=" ")
    print()


    