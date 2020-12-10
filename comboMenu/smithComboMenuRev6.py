from typing import ItemsView
import useful
from Order import Order

useful.Terminal.clear()
ITEMS = {
    "krabby patty" : {"no cheese" : 1.25, "cheese" : 1.50},
    "double krabby patty" : {"no cheese" : 2.00, "cheese" : 2.25},
    "triple krabby patty" : {"no cheese" : 3.00, "cheese" : 3.25},
    "coral bits" : {"small" : 1.00, "medium" : 1.25, "large" : 1.50},
    "kelp rings" : {"no sauce" : 1.50, "sauce" : 2.00},
    "krabby meal" : 3.50,
    "double krabby meal" : 3.75,
    "triple krabby meal" : 4.00,
    "salty sea dog" : 1.25,
    "footlong" : 2.00,
    "sailors surprise" : 3.00,
    "golden loaf" : {"no sauce" : 2.00, "sauce" : 2.50},
    "kelp shake" : 2.00,
    "seafoam soda" : {"small" : 1.00, "medium" : 1.25, "large" : 1.50},
    "krusty krab pizza" : {"6 inch" : 2.50, "12 inch" : 3.00, "16 inch" : 3.75}
    }

def menu(items):
    menuStr = ""
    for i in items:
        menuStr += useful.Terminal.Color.CYAN + i + useful.Terminal.Color.END
        if type(items[i]) == dict:
            menuStr += "\n"
            for j in items[i]:
                menuStr += "    " + useful.Terminal.Color.PURPLE + j + useful.Terminal.Color.END + "\t" + useful.Terminal.Color.BLUE + useful.Strings.formatAsMoney(items[i][j]) + useful.Terminal.Color.END + "\n"
            
        else:
            menuStr += "    " + useful.Terminal.Color.BLUE + useful.Strings.formatAsMoney(items[i]) + useful.Terminal.Color.END + "\n"
        menuStr += "\n"
    # print(menuStr)
    menuLst = menuStr.split("\n\n")
    menuLst.pop(len(menuLst) - 1)
    # print(useful.lstToStr(menuLst, "\n"))
    for i in range(len(menuLst)):
        # print(menuLst[i])
        menuLst[i] = menuLst[i].split("\n")
        # print(useful.lstToStr(menuLst[i], "\n"))
    return menuLst
MENUITEMS = menu(ITEMS)




"""
    ╔════════════════════════════════════════════════════════════════════════╗
    ║    __                     ___              __     _             _      ║
    ║   /  \    /\    |   |    |      \ /       /  \   |_\  |   |    | |     ║
    ║   |  _   /__\   |   |    |--     |        |  _   |\   |   |    |-<     ║
    ║   \__/  /    \  |__ |__  |___    |        \__/   | \  \___/    |__|    ║
    ║                                                                        ║
    ╠════════════════════════════════════════════════════════════════════════╣
    ║                                                                        ║
    ║krabby patty                                    krabby meal    $3.50    ║
    ║    no cheese  $1.25                     double krabby meal    $3.75    ║
    ║    cheese     $1.50                     triple krabby meal    $4.00    ║
    ║                                                                        ║
    ║double krabby patty                           salty sea dog    $1.25    ║
    ║    no cheese  $2.00                               footlong    $2.00    ║
    ║    cheese     $2.25                       sailors surprise    $3.00    ║
    ║                                                                        ║
    ║triple krabby patty                             golden loaf             ║
    ║    no cheese  $3.00                                no sauce   $2.00    ║
    ║    cheese     $3.25                                sauce      $2.50    ║
    ║                                                                        ║
    ║coral bits                                       kelp shake    $2.00    ║
    ║    small      $1.00                                                    ║
    ║    medium     $1.25                           seafoam soda             ║
    ║    large      $1.50                               small       $1.00    ║
    ║                                                   medium      $1.25    ║
    ║kelp rings                                         large       $1.50    ║
    ║    no sauce   $1.50                                                    ║
    ║    sauce      $2.00                                                    ║
    ║                                                                        ║
    ╚════════════════════════════════════════════════════════════════════════╝
"""
# below print statement prints something like above comment, but with Colored text
MENU = f"""╔════════════════════════════════════════════════════════════════════════╗
║{useful.Terminal.Color.RED}    __                     ___              __     _             _      {useful.Terminal.Color.END}║
║{useful.Terminal.Color.RED}   /  \    /\\    |   |    |      \\ /       /  \   |_\  |   |    | |     {useful.Terminal.Color.END}║
║{useful.Terminal.Color.RED}   |  _   /__\\   |   |    |--     |        |  _   |\   |   |    |-<     {useful.Terminal.Color.END}║
║{useful.Terminal.Color.RED}   \\__/  /    \\  |__ |__  |___    |        \\__/   | \  \\___/    |__|    {useful.Terminal.Color.END}║
║                                                                        ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║{MENUITEMS[0][0]}                                    {MENUITEMS[5][0]}    ║
║{MENUITEMS[0][1]}                     {MENUITEMS[6][0]}    ║
║{MENUITEMS[0][2]}                     {MENUITEMS[7][0]}    ║
║                                                                        ║
║{MENUITEMS[1][0]}                           {MENUITEMS[8][0]}    ║
║{MENUITEMS[1][1]}                               {MENUITEMS[9][0]}    ║
║{MENUITEMS[1][2]}                       {MENUITEMS[10][0]}    ║
║                                                                        ║
║{MENUITEMS[2][0]}                             {MENUITEMS[11][0]}             ║
║{MENUITEMS[2][1]}                            {MENUITEMS[11][1]}    ║
║{MENUITEMS[2][2]}                            {MENUITEMS[11][2]}    ║
║                                                                        ║
║{MENUITEMS[3][0]}                                       {MENUITEMS[12][0]}    ║
║{MENUITEMS[3][1]}                                                    ║
║{MENUITEMS[3][2]}                           {MENUITEMS[13][0]}             ║
║{MENUITEMS[3][3]}                           {MENUITEMS[13][1]}    ║
║                                               {MENUITEMS[13][2]}    ║
║{MENUITEMS[4][0]}                                     {MENUITEMS[13][3]}    ║
║{MENUITEMS[4][1]}                                                    ║
║{MENUITEMS[4][2]}                                                    ║
║                                                                        ║ 
╚════════════════════════════════════════════════════════════════════════╝"""





subTotal = 0
useful.Terminal.clear()
order = Order.place(MENU, ITEMS)
subTotal = Order.subTotal


changeCommands = {"add" : "Order.add(order, MENU, ITEMS)",
    "edit" : "Order.edit(order, MENU, ITEMS)",
    "remove" : "Order.remove(order, MENU, ITEMS)"
}

while True:
    useful.Terminal.clear()
    print( useful.Strings.lstToStr(order, "\n") )
    print("Subtotal:", useful.Terminal.Color.PURPLE + useful.Strings.formatAsMoney(subTotal) + useful.Terminal.Color.END)

    ui = input(f"What do you want to do: {useful.Strings.lstToStr(changeCommands, ', ', False)}, or type done if you are done: {useful.Terminal.Color.WHITE}")
    print(useful.Terminal.Color.END, end = "")
    if ui in changeCommands:
        order = eval( changeCommands[ui] )
        subTotal = Order.subTotal
    elif ui == "done":
        break



subTotal = useful.Maths.tax(subTotal, 7)
print("After tax", useful.Terminal.Color.PURPLE + useful.Strings.formatAsMoney(subTotal) + useful.Terminal.Color.END)
possibleTips = ("10", "15", "20")
tip = input("What percent tip {}, you don't need a percent sign: ".format(useful.Strings.lstToStr(possibleTips, ", ", False)) + useful.Terminal.Color.WHITE)

while not useful.Terminal.inputChecker(tip, possibleTips):
    tip = useful.Terminal.inputInt(useful.Terminal.Color.END + "What percent tip {}, you don't need a percent sign: ".format(useful.Strings.lstToStr(possibleTips, ", ", False)) + useful.Terminal.Color.WHITE)
print(useful.Terminal.Color.END, end = "")
total = useful.Maths.tax(subTotal, int(tip))

print(useful.Terminal.Color.PURPLE + useful.Strings.formatAsMoney(total) + useful.Terminal.Color.END)

