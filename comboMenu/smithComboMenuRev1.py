print("Welcome to Good Burger, may I take your order?")
total = 0
order = ""
samich = input("What kind of sandwhich do you want (chicken(c) for $5.25, beef(b) for $6.25, tofu(t) for $5.75) ")
drink = input("Do want something to drink? (y/n) ")
if (samich == "c"):
    total += 5.25
    samich = "Chicken"
elif (samich == "b"):
    total += 6.25
    samich = "Beef"
elif (samich == "t"):
    total += 5.75
    samich = "Tofu"
if (drink == "y"):
    drink = input("What size? (small(s) $1.00, medium(m) $1.75, large(l) $2.25 ")
    if (drink == "s"):
        total += 1
        drink = "small"
    elif (drink == "m"):
        total += 1.75
        drink = "medium"
    elif (drink == "l"):
        total += 2.25
        drink = "large"
    else:
        drink = "No"
else:
    drink = "No drink"

order = order + samich + " sandwich, " + drink + " drink "
print(order)
print("Your total is", total)