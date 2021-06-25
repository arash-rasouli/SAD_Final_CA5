from datetime import  *
daily_cost = 5

class Insurance:
    def __init__(self, insuranceId):
        self.insuranceId = insuranceId
        self.name = "insuranceCompany"
        self.startDate = 0
        self.endDate = 0
        self.contract = "contract"
        self.cost = 0

    def setValidationTime(self, startDate, endDate):
        self.startDate = startDate
        self.endDate = endDate
        self.calculateCost()
        
    def calculateCost(self):
        self.cost = 200 + ((self.endDate - self.startDate).days) * daily_cost
    
    def getCost(self):
        return self.cost
    
    
