print("=== Grocery billing tool ===")


low_price_item = 0
medium_price_item = 0 
high_price_item = 0


customers_Served = 0 
total_sales = 0

billing = True


while billing:
    name = input("Enter the customers name: ")
    items_buying = int(input(f"How much items you are buying {name}?: "))
    if items_buying <=  0:
        print("The number is less than 1. Please try again!")
        continue

    customer_total = 0 
    item_number = 1

    while item_number <= items_buying:
        item_name = input("Item name: ")
        item_price = int(input("Item price: "))
        quantity = int(input("Quantity of the item:"))

        if item_price <= 0 or quantity <= 0:
            print("Invalid price or quantity, Please enter it again.\n")
            continue
        item_total = item_price * quantity 
        print(f" {item_name}: {quantity} x {item_price} = {item_total}")

        customer_total += item_total

        if item_price < 50:
            low_price_item += quantity
        elif item_price <= 100:
            medium_price_item += quantity
        else:
            high_price_item += quantity
        
        item_number += 1 

    customers_Served += 1
    total_sales += customer_total

    print(f"\n Total bill for {name}: {customer_total} ")
    print("Billing Complete! \n")

    again = input("Next Customer? (yes/no): ")

    if again != "yes":
        billing = False

print("\n === Grocery Category Report ===")

for slot in range (1,4):
    if slot == 1:
        label, total, = "Low price items", low_price_item
    elif slot == 2:
        label, total, = "Medium price items", medium_price_item
    else:
        label, total, = "High price items", high_price_item

    if total > 0:
        print(f" {label}: {total} ", end="")

        for item in range(total):
            print("*", end="" )

        print()

print(f"\n Customers Served: {customers_Served}")
print(f"Total sales:  {total_sales} ")
print("Grocery billing closed. Goodbye!")