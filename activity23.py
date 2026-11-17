#part 1
passengers = ["Ana","Ben","Carla"]
passengers.append("Dan")
passengers.insert(0,"Lola")
passengers.remove("Ben")
x = passengers.pop( )
y = passengers.pop(0)
len(passengers)
"Ana" in passengers
passengers.reverse()

#part 2
route = ["Terminal","Perez park","Pacific Mall"]
passengers = []
SEAT = 6
FARE = 13
total = 0

while True:
    print()
    print("Sakay", passengers)
    print(len(passengers),"of",SEAT,"Seats")
    print("4 baba sa pinto 5 baba sa harap")
    print("6 seat check 7 balikan 8 Exit")
    choice = input("choice")
    
    if choice == "1":
        if len(passengers == SEAT):  
            print("Puno na!")
        else:
            name = input("NAME:")
            passengers.append(name)
            total = total + FARE
            print(name,"Borded at the back")        
        
    elif choice == "2":
        if len(passengers == SEAT):
            print("Puno na!")
        else:
            name =input("Name:")
            passengers.insert(name)
            total = total + FARE
            print(name,"Priority Seat")    
            
    elif choice == "3":
        name=input("Who's getting off?") 
        if name in passengers:
           passengers.remove(name)
           print(name, "got of, Ingat!")
        else:
            print(name,"is not on the jeep")
            
    elif choice == "4":
        if len(passengers) == 0:
           print("The jeep is empty")
        else:
            left = passengers.pop()
            print(left,"Got off at the front")
    
    elif choice == "5":
        if len(passengers) == 0:
            print("The jeep is empty")
        else: 
            front = passengers.pop(0)
            print(front, "got off at the front")
    
    elif choice == "6":
        for i in range(len(passengers)):
            print("SEAt", i + 1, passengers[i])
    elif choice == "7":
        route.reverse()
        print("ROUTE:",route)
    elif choice == "8":
        print("Total fare today:",total) 
    else:
        print("INVALID CHOICE.")      
        
    
                  
                    
            