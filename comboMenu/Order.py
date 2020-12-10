import useful


class Order:

    subTotal = 0
    def place(MENU, ITEMS):
        thisOrder = []
        print(MENU)
        ui = input("Welcome to The Krusty Krab, may I take your order? " + useful.Terminal.Color.WHITE)
        while True:
            print(useful.Terminal.Color.END, end = "")
            if ui in ITEMS:
                thisOrder.append(Order.checkMenuForItem(ITEMS, ui))
            elif ui == "done":
                return thisOrder
            else:
                print(f"{useful.Terminal.Color.RED}{ui} is not on the menu.{useful.Terminal.Color.END}")
            print(f"{useful.Terminal.Color.PURPLE}subtotal{useful.Terminal.Color.END} {useful.Terminal.Color.BLUE}{useful.Strings.formatAsMoney(Order.subTotal)}{useful.Terminal.Color.END}")
            ui = input("Anything else, type done if your done? " + useful.Terminal.Color.WHITE)

    def edit(order, MENU, ITEMS):
        orderCopy = order.copy()

        for i in range(len(orderCopy)):
            orderCopy[i] = f"Item {str(i + 1)}: {str(useful.Strings.lstToStr(orderCopy[i]))}\n"

        print(useful.Strings.lstToStr(orderCopy, "\n"))
        numToEdit = useful.Terminal.inputInt("What item do you want to edit? " + useful.Terminal.Color.WHITE) - 1
        print(useful.Terminal.Color.END, end = "")

        if order[numToEdit][0] in ITEMS:
            Order.subTotal -= ITEMS[order[numToEdit][0]]
        elif order[numToEdit][1] in ITEMS and order[numToEdit][0] in ITEMS[order[numToEdit][1]]:
            Order.subTotal -= ITEMS[ order[numToEdit][1] ][ order[numToEdit][0] ]

        print(MENU)
        while True:
            newItem = input(f"What item do you want to replace item {numToEdit + 1} with? " + useful.Terminal.Color.WHITE)
            if newItem != ["fail"]:
                order[numToEdit] =  Order.checkMenuForItem(ITEMS, newItem)
                break
            else:
                print(f"{useful.Terminal.Color.RED}{ui} is not on the menu.{useful.Terminal.Color.END}")
        print(useful.Terminal.Color.END, end = "")
        
        return order

    def add(order, MENU, ITEMS):
        print(MENU)

        ui = input("What do you want to add to the order? " + useful.Terminal.Color.WHITE)
        while True:
            print(useful.Terminal.Color.END, end = "")
            print(MENU)
            if ui in ITEMS:
                order.append(Order.checkMenuForItem(ITEMS, ui))
                return order
    
    def remove(order, MENU, ITEMS):
        orderCopy = order.copy()

        for i in range(len(orderCopy)):
            orderCopy[i] = f"Item {str(i + 1)}: {str(useful.Strings.lstToStr(orderCopy[i]))}\n"
        
        print(useful.Strings.lstToStr(orderCopy, '\n'))
        
        numToRemove = useful.Terminal.inputInt("What item do you want to remove from the order? " + useful.Terminal.Color.WHITE) - 1
        print(useful.Terminal.Color.END, end = "")

        if order[numToRemove][0] in ITEMS:
            Order.subTotal -= ITEMS[order[numToRemove][0]]
        elif order[numToRemove][1] in ITEMS and order[numToRemove][0] in ITEMS[order[numToRemove][1]]:
            Order.subTotal -= ITEMS[ order[numToRemove][1] ][ order[numToRemove][0] ]

        order.pop(numToRemove)
        return order


    def checkMenuForItem(ITEMS, ui):
        thisOrder = ["fail"]
        if type(ITEMS[ui]) == float:
            Order.subTotal += ITEMS[ui]
            thisOrder = [ui]
        elif type(ITEMS[ui]) == dict:
            options = "options:"
            for i in ITEMS[ui]:
                options += f"\n    {useful.Terminal.Color.PURPLE}{i}{useful.Terminal.Color.END}   {useful.Terminal.Color.BLUE}"
                options += f"{useful.Strings.formatAsMoney(ITEMS[ui][i])}{useful.Terminal.Color.END}"
            while True:
                ui2 = input(options + "\n    " + useful.Terminal.Color.WHITE)
                print(useful.Terminal.Color.END, end = "")
                if ui2 in ITEMS[ui]:
                    Order.subTotal += ITEMS[ui][ui2]
                    thisOrder = [ui2, ui]
                    break
                else:
                    print(f"{ui2} is not an option of this item.")
        return thisOrder

