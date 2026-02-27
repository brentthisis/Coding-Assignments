total_bill = 0
receipt = ""
print("\nWelcome to our Restaurant!")

while True:     # The while true statement creates an infinite loop since the condition remains True in each iteration.

    print("\n------ Menu ------")
    print("1. Burger - 25 AED")
    print("2. Pizza - 30 AED")
    print("3. Pasta - 18 AED")
    print("4. Sandwich - 12 AED")
    print("5. Coffee - 10 AED")

    # For choosing item
    while True:
        try:        # The try function tests if there are errors in the input such as putting in a string when an integer is expected
            choice = int(input("\nEnter item number (1-5): "))

            if 1<= choice <= 5:     # In this case, if the choice is between 1 and 5 and is not 0 or a negative integer, the loop breaks and executes the next lines of code. This is for validation.
                break
            else:
                print("\nInvalid option. Please input a number between 1 and 5.")

        except ValueError:
            print("\nInvalid input. Please input a valid number.")
    
    # For choosing quantity
    while True:
        try:
            quantity = int(input("\nEnter quantity: "))
            if quantity > 0:
                break
            else:
                print("\nInvalid amount. Please input a valid quantity.")

        except ValueError:
            print("\nInvalid input. Please input a valid number.")

    # Controls the price of each item
    if choice == 1:
        item_name = "Burger"
        price = 25
    elif choice == 2:
        item_name = "Pizza"
        price = 30
    elif choice == 3:
        item_name = "Pasta"
        price = 18
    elif choice == 4:
        item_name = "Sandwich"
        price = 12
    elif choice == 5:
        item_name = "Coffee"
        price = 10

    item_total = price * quantity
    total_bill += item_total

    receipt += item_name + " - " + str(quantity) + " * " + str(price) + " AED = " + str(item_total) + " AED\n" # Handles multiple orders

    print("\nAdded:", item_name, "-", quantity, "*", price, "AED =", item_total, "AED")
    print("Current Total:", total_bill, "AED")

    # Controls if the customer wants to order again
    while True:
        again = input("\nDo you want to order another item? (yes/no): ").lower() # .lower() Converts uppercase letters to lowercase
        if again == "yes":
            break
        elif again == "no":
            break
        else:
            print("\nInvalid input, please type yes or no.")
    if again == "no":
        break

print("\n------Receipt------")
print(receipt)

# For handling payment
while True:
    try:
        print("\nFinal Total Bill:", total_bill, "AED")
        payment = int(input("Enter payment amount (AED): "))
        
        if payment < total_bill:
            print("\nInsufficient payment. You still require", total_bill - payment, "AED.")
        elif payment > total_bill:
            print("\nYour change is:", payment - total_bill, "AED")
            print("Thank you for dining with us!\n")
            break
        else:
            print("\nPayment complete!")
            print("Thank you for dining with us!\n")
            break

    except ValueError:
        print("\nInvalid payment amount. Please enter a valid payment amount.")
