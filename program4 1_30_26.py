def calculate_total_purchase():
    # A customer in a store is purchasing five items.
    # Write a program that asks for each item,
    # then displays the subtotal of the sale,
    # the amount of sales tax, and the total.
    # Assume the sales tax is 7 percent.

    # Get item prices from the user
    item1 = float(input("Enter price of item 1: "))
    item2 = float(input("Enter price of item 2: "))
    item3 = float(input("Enter price of item 3: "))
    item4 = float(input("Enter price of item 4: "))
    item5 = float(input("Enter price of item 5: "))

    # Calculate subtotal
    subtotal = item1 + item2 + item3 + item4 + item5

    # Calculate sales tax (7%)
    tax_rate = 0.07
    sales_tax = subtotal * tax_rate

    # Calculate total
    total = subtotal + sales_tax

    # Print results
    print("Subtotal: $", format(subtotal, ".2f"), sep="")
    print("Sales Tax (7%): $", format(sales_tax, ".2f"), sep="")
    print("Total: $", format(total, ".2f"), sep="")

# Line which calls the above function.
calculate_total_purchase()