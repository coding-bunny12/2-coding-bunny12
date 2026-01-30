def average_age():
    # Get User Input
    age1 = float(input("Enter age of friend 1: "))
    age2 = float(input("Enter age of friend 2: "))
    age3 = float(input("Enter age of friend 3: "))
    age4 = float(input("Enter age of friend 4: "))
    age5 = float(input("Enter age of friend 5: "))

    # Sum ages
    total = age1 + age2 + age3 + age4 + age5
    # Average the ages
    average = total / 5
    # Print the results
    print("The average is:", average)
# Line which calls the above function.
average_age()
