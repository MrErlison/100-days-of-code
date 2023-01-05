
QUARTERS = 0.25
DIMES = 0.1
NICKLES = 0.05
PENNIES = 0.01

def printMachineReport(charge, stock):
    print(f"\nTotal chage: US${charge}")
    print("Total ingredients:")
    for item in stock:
        print(f"\t{item.title()}:\t{stock[item]}")
    print("")

def printChoice(choice, details):
    print("Your choice:")
    print(f"\tDrink:\t{choice.title()}")
    for m in details['ingredients']:
        print(f"\t{m.title()}:\t{details['ingredients'][m]}ml")
    print(f"\tCost:\tUS${details['cost']}\n")        

def processCoins(cost):
    print("Please insert coins.")
    coins  = float(input("how many US$0.25 (quarters)?: ")) * QUARTERS
    coins += float(input("how many US$0.1 (dimes)?: ")) * DIMES
    coins += float(input("how many US$0.05 (nickles)?: ")) * NICKLES
    coins += float(input("how many US$0.01 (pennies)?: ")) * PENNIES
    return coins

def checkTransaction(cost):
    payment = processCoins(cost)
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"Here is ${change} in change.")
        return cost

    print("Sorry that's not enough money. Money refunded.")
    return -1

def checkResources(ingredients, stock):
    """controle do estoque, podendo adicionar ou retirar"""
    for item in ingredients:
        if ingredients[item] > stock[item]:
            print(f"Sorry there is not enough {item}.")
            return False

    return True

def selectDrink():
    menu = {
        "black": {
            "ingredients": {"water": 50, "coffee": 14, }, 
            "cost": 1.0,},        
        "espresso": {
            "ingredients": {"water": 50, "coffee": 18, }, 
            "cost": 1.5,},
        "latte": {
            "ingredients": {"water": 200, "coffee": 24, "milk": 150,},
            "cost": 2.5,},
        "cappuccino": {
            "ingredients": {"water": 250, "coffee": 24, "milk": 150,},
            "cost": 3.0,}
    }
    choice = 'on'

    options = [m.title() for m in menu]
    while choice != 'off':
        choice = input(f"What would you like? {'/'.join(options)} => ").lower()
        if choice in menu:
            printChoice(choice, menu[choice])
            return menu[choice]
        print(f"Sorry. I didn't understand your choice.")
    
    print("Turn off the Coffee Machine.")
    exit(0)

def makeCoffee(drink, charge, stock):
    ingredients = drink['ingredients']
    for item in ingredients:
        stock[item] -= ingredients[item]

    printMachineReport(charge, stock)

    return stock


def coffee():
    stock = {'water':1000, 'milk': 1000, 'coffee': 1000}
    charge = 1000.00

    print("\nCoffee Machine is Open")
    printMachineReport(charge, stock)

    while True:    
        drink = selectDrink()
        cost = drink['cost']
        ingredients = drink['ingredients']

        print(ingredients)

        if not checkResources(ingredients, stock):
            continue

        bill = checkTransaction(cost)
        if bill < 0:
            continue
        
        charge += bill
        
        stock = makeCoffee(drink, charge, stock)

if __name__ == "__main__":
    coffee()
