class Address:
    def __init__(self, city, region, street, alley, number):
        self.city = city
        self.region = region
        self.street = street
        self.alley = alley
        self.number = number

class Site:
    def __init__(self):
        self.floorNum = 0
        self.isResidential = True
        self.address = None
    
    def setFloorNum(self, floorNum):
        self.floorNum = floorNum

    def setResidentalStatus(self, ResOrNot):
        self.isResidential = ResOrNot
        
    def makeAddress(self, addr):
        addr = addr.split("/")
        newAddr = Address(addr[0], addr[1], addr[2], addr[3], addr[4])
        self.address = newAddr