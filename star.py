print("Half pyramid Pattern number of Stars")

n = int(input(" Enter number of stars: "))


for i in range(n):
    for j in range(i+1):
        print("*", end = " ")
    print()
    