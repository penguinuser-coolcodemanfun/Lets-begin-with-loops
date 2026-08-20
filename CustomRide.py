print("============================================")
print("         Welcome to Ride Builder            ")
print("============================================")
print()


print("Step 1: Pick your Vehicle")
print(" 1 - Bike")
print(" 2 - Car ")
print()

choice = int(input("Enter 1 or 2: "))
print()

if choice == 1:
    print("Step 2: Pick your bike type")
    print(" 1 - Scooty ")
    print(" 2 - Mountain Bike")
    print()

    bike_type = int(input("Enter 1 Or 2: "))
    print()

    if bike_type == 1:
        print("You picked   : Scooty")
        print("Top speed    : 80 km/h ")
        print("Best for     : City roads")
    else:
        print("You picked    : Mountain Bike")
        print("Top speed     : 40 km/h")
        print("Best for      : Off-Road trails")

elif choice == 2:
    print(" Step 2: Pick your car type")
    print(" 1 - sedan")
    print(" 2 - suv ")

    car_type = int(input(" Enter 1 or 2:  "))
    print()

    if car_type == 1:
        print("You picked    : Sedan")
        print("Seats         : 5 passengers ")
        print("Best for      : Family Trips")
    else:
        print("You picked    : SUV")
        print("Seats         : 7 passengers ")
        print("Best for      : Off-Road Trips")
else:
    print("That was not a vaild choice.")
    print("Please enter 1 for bike or 2 for car.")

print()
print("==========================================")
print("      Your custom ride is ready           ")
print("      Enjoy the Journey                   ")
print("==========================================")



        

