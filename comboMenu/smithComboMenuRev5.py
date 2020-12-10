def clear(): 
    from os import system, name
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

clear()



print("Welcome to The Krusty Krab, may I take your order?\n")
total = 0
order = []
discountS = False
discountD = False
discountF = False
discount = ""

samich = input("What kind of sandwhich do you want (chicken(c) for $5.25, beef(b) for $6.25, tofu(t) for $5.75, (n) for no sandwich) ")
drink = input("Do want something to drink? (y/n) ")
fries = input("Do you want fries? (y/n) ")
ketchup = int(input("How many ketchup packets do you want? $0.25 per packet ")) #ketchup packets
total += abs(ketchup * 0.25)

if (samich == "c"):
    total += 5.25
    order.append("Chicken")
    discountS = True
elif (samich == "b"):
    total += 6.25
    order.append("Beef")
    discountS = True
elif (samich == "t"):
    total += 5.75
    order.append("Tofu")
    discountS = True
else:
    order.append("No")


if (drink == "y"):
    drink = input("What size drink? (small(s) $1.00, medium(m) $1.75, large(l) $2.25, child(c) $2.63 ")
    if (drink == "s"):
        total += 1
        order.append("small")
    elif (drink == "m"):
        total += 1.75
        order.append("medium")
    elif (drink == "l"):
        total += 2.25
        order.append("large")
    elif (drink == "c"):
        total += 2.63
        order.append("child size")
    else:
        order.append("No")
    discountD = True
else:
    order.append("No")

if (fries == "y"):
    fries = input("What size fry, small(s) for $1.00, medium(m) for $1.50, large(l) for $2.00 ")
    if (fries == "s"):
        total += 1
        order.append("small")
    elif (fries == "m"):
        total += 1.5
        order.append("medium")
    elif (fries == "l"):
        total += 2
        order.append("large")
        if (input("Do you want to child-size your fry for $0.38 more? (y/n) ") == "y"):
            total += 0.38
            order.append("child size")
    discountF = True
else:
    order.append("No")

order.append(ketchup)

if (discountD and discountF and discountS):
    total -= 1
    discount = "Combo discount $1.00"




print("""
Your order is a {0} sandwich,
a {1} drink,
a {2} fry,
and {3} ketchup packet(s)
for a total of {4}
""".format(order[0],order[1],order[2],order[3],('${:,.2f}'.format(total))))

