print("Welcome to Python Pizza deliveries!")
size = raw_input("What size pizza do you want? Enter S, M, or L: ")
pepperoni = raw_input("Would you like to add pepperoni? Y or N: ")
cheese = raw_input("Would you like extra cheese? Y or N: ")
price = 0

if size == "S":
    price += 15
    if pepperoni == "Y":
        price += 2
elif size == "M":
    price += 20
    if pepperoni == "Y":
        price += 3
elif size == "L":
    price += 25
    if pepperoni == "Y":
        price += 3
else:
    print("Incorrect input. Restart program and try again. Be sure to capitalize your responses.")

if cheese == "Y":
    price += 1

print("You final bill is $" + str(price))