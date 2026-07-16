class MoneyMachine:

    def __init__(self):
        self.profit = 0

    def report(self):
        return self.profit

    def make_payment(self, amount, cost):

        if amount >= cost:

            self.profit += cost

            return True, amount - cost

        return False, amount