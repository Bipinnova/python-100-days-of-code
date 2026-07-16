class CoffeeMaker:

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        return self.resources

    def is_resource_sufficient(self, drink):

        for item in drink.ingredients:

            if drink.ingredients[item] > self.resources[item]:
                return False, f"Not enough {item}"

        return True, "Enough resources"

    def make_coffee(self, drink):

        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]

        return f"{drink.name} is ready."