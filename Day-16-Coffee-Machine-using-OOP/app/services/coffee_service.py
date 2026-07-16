from app.models.menu import Menu
from app.models.coffee_maker import CoffeeMaker
from app.models.money_machine import MoneyMachine


class CoffeeService:

    def __init__(self):

        self.menu = Menu()
        self.coffee_maker = CoffeeMaker()
        self.money_machine = MoneyMachine()

    def get_menu(self):

        return self.menu.get_items()

    def report(self):

        resources = self.coffee_maker.report()

        return {
            "resources": {
                "water": f"{resources['water']} ml",
                "milk": f"{resources['milk']} ml",
                "coffee": f"{resources['coffee']} grams"
            },
            "profit": f"₹{self.money_machine.report()}"
        }

    def order(self, drink_name, amount):

        drink = self.menu.find_drink(drink_name)

        if drink is None:

            return {
                "success": False,
                "message": "Drink not found",
                "change": amount
            }

        ok, message = self.coffee_maker.is_resource_sufficient(drink)

        if not ok:

            return {
                "success": False,
                "message": message,
                "change": amount
            }

        paid, change = self.money_machine.make_payment(amount, drink.cost)

        if not paid:

            return {
                "success": False,
                "message": "Insufficient money",
                "change": amount
            }

        coffee_message = self.coffee_maker.make_coffee(drink)

        return {
            "success": True,
            "message": coffee_message,
            "change": change
        }


coffee_service = CoffeeService()