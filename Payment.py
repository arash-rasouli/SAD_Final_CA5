class Payment:
    def __init__(self, _id):
        self.id = _id
        self.cost = 0
        self.paid = 0
        self.deposit = 0
    
    def setCost(self, cost):
        self.cost = cost
        self.calculateDeposit()

    def setPaid(self, amount):
        self.paid += amount
    
    def calculateDeposit(self):
        self.deposit = 0.3 * self.cost