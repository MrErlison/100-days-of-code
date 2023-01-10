from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee():
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    menu = Menu()

    while True:
        options = menu.get_items()
        choice = input(f"What would you like? ({options}): ")
        if choice == "off":
            break
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
            continue

        drink = menu.find_drink(choice)

        # Verifica se há recursos suficientes no coffee_maker e se o pagamento foi realizado com sucesso
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

    coffee_maker.report()
    money_machine.report()

if __name__ == "__main__":
    coffee()