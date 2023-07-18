from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

mrcoffee = CoffeeMaker()
mrmenu = Menu()
givemoney = MoneyMachine()


def coffee_machine():
	power_on = False
	while not power_on:

		chosen_drink = input(f"Hi, please choose a drink {mrmenu.get_items()}. ")

		if chosen_drink == "report":
			mrcoffee.report()
			givemoney.report()
			continue

		found_drink = mrmenu.find_drink(chosen_drink)
		print(found_drink)
		if mrcoffee.is_resource_sufficient(found_drink):
			givemoney.make_payment(found_drink.cost)
			mrcoffee.make_coffee(found_drink)


coffee_machine()
