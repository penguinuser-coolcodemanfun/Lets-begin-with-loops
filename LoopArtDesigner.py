print("===== STAR PYRAMID PATTERN =====")

rows = int(input("Enter number of rows for star pattern:"))

for i in range(rows):
    for j in range(i + 1):
        print("* ", end="")
    print()
    
print("===== FLOYDS TRIANGLE =====")

rows = int(input("Enter the number of rows for Floyds Triangle"))
number = 1

for i in range(1, rows, + 1):
    for j in range(1, i + 1):
        print(number, end=" ")
        number += 1
    print()

print("===== DIAMOND NUMBER PATTERN =====")

row_size = int(input("Enter number of rows for diamond pattern: "))
half = (row_size // 2) + 1

# Top half
for i in range(1, half + 1):
    print(" " * (half - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Bottom half
for i in range(half - 1, 0, -1):
    print(" " * (half - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("===== LOOP ART DESIGN COMPLETE! ===== ")
print("you created star, triangle and diamond patterns using nested loops!")
    


