class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("espresso", 50, 0, 18, 125),
            MenuItem("latte", 200, 150, 24, 200),
            MenuItem("cappuccino", 250, 50, 24, 250),
        ]

    def get_items(self):
        return [
            {
                "name": item.name,
                "price": item.cost
            }
            for item in self.menu
        ]

    def find_drink(self, name):
        for item in self.menu:
            if item.name.lower() == name.lower():
                return item
        return None