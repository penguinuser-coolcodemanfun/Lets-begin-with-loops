print("===== HOLIDAY ACTIVITY PLANNER =====")

print(" Pick your holiday type:")
print(" 1: Beach Holiday")
print("     ")
print(" 2: Mountain Holiday")

choice = int(input("Enter 1 or 2:   "))


if choice == 1:
    print("Pick your beach activity")
    print(" 1: Swimming ")
    print("     ")
    print(" 2: Sandcastle Building")

    beach_activity = int(input("Choose 1 or 2:  "))
    if beach_activity == 1:
        print("You picked : Swimming")
        print(" Best time : Morning")
        print(" Remember to put sunscreen and bring water!")

elif choice == 2:
        print("Pick your mountain activity:")
        print(" 1: Hiking")
        print("     ")
        print(" 2: Camping")

        mountain_activity = int(input("Choose 1 or 2"))
        
        

        if mountain_activity == 1:
            print("You picked: Hiking")
            print("Best for: Exploring trails")
            print("Remember to wear comfortable shoes!")
        else:
            print("You picked: Camping")
            print("Best for: Staying close to nature")
            print("Remember: Carry a Tent and Flashlight")
else:
        print("That was not a valid choice")
        print("Choose 1 for Hiking and 2 for Camping.")

print(" ===== Your holiday plan is ready! =====")
print(" ===== Enjoy your holiday! =====")
