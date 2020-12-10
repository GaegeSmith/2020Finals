print("Welcome to Good Burger, may I take your order?\n")
total = 0
order = ""
discountS = False
discountD = False
discountF = False
discount = ""

samich = input("What kind of sandwhich do you want (chicken(c) for $5.25, beef(b) for $6.25, tofu(t) for $5.75, (n) for no sandwich) ")
drink = input("Do want something to drink? (y/n) ")
fries = input("Do you want fries? (y/n) ")
total += abs(int(input("How many ketchup packets do you want? $0.25 per packet ")) * 0.25) #ketchup packets

if (samich == "c"):
    total += 5.25
    samich = "Chicken"
    discountS = True
elif (samich == "b"):
    total += 6.25
    samich = "Beef"
    discountS = True
elif (samich == "t"):
    total += 5.75
    samich = "Tofu"
    discountS = True


if (drink == "y"):
    drink = input("What size drink? (small(s) $1.00, medium(m) $1.75, large(l) $2.25, child(c) $2.63 ")
    if (drink == "s"):
        total += 1
        drink = "small"
    elif (drink == "m"):
        total += 1.75
        drink = "medium"
    elif (drink == "l"):
        total += 2.25
        drink = "large"
    elif (drink == "c"):
        total += 2.63
        drink = "child size"
    else:
        drink = "No"
    discountD = True
else:
    drink = "No"

if (fries == "y"):
    fries = input("What size fry, small(s) for $1.00, medium(m) for $1.50, large(l) for $2.00 ")
    if (fries == "s"):
        total += 1
        fries = "small"
    elif (fries == "m"):
        total += 1.5
        fries = "medium"
    elif (fries == "l"):
        total += 2
        fries = "large"
        if (input("Do you want to child-size your fry for $0.38 more? (y/n) ") == "y"):
            total += 0.38
            fries = "child size"
    discountF = True
else:
    fries = "No"


if (discountD and discountF and discountS):
    total -= 1
    discount = "Combo discount $1.00"





order = order + samich + " sandwich, " + drink + " drink, " + fries + " fry, " + discount + " "
print(order)
print('${:,.2f}'.format(total))
