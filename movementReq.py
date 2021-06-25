from Site import *
from heavyStuff import *
from MovementTeam import *
from Payment import *
from Insurance import *
from datetime import  *

class Request:
    def __init__(self, requestId, userId):
        self.requestId = requestId
        self.userId = userId
        self.insurance = None
        self.totalCost = 0
        self.makeInsurance()
        
    def makeInsurance(self):
        self.insurance = Insurance(self.requestId)

    def getTotalCost(self):
        return self.totalCost
    
class MovementReq(Request):
    def __init__(self, requestId, userId, heavyStufCatInstance, EmployeeCatalogInstance, Payment):
        super().__init__(requestId, userId)
        self.startDate = None
        self.endDate = None
        self.beginSite = None
        self.destSite = None
        self.heavyStuffCatalog = heavyStufCatInstance
        self.movementTeam = MovementTeam(EmployeeCatalogInstance)
        self.heavyStuffIds = []
        self.payment = Payment
        
    def setDateTimes(self, start, end):
        start = start.split('/')
        end = end.split('/')
        self.startDate = datetime(int(start[0]), int(start[1]), int(start[2]), int(start[3]))
        self.endDate = datetime(int(end[0]), int(end[1]), int(end[2]), int(end[3]))

    def makeSites(self, srcAddr, destAddr):
        newSiteSrc = Site()
        newSiteSrc.makeAddress(srcAddr)
        self.beginSite = newSiteSrc
        
        newSiteDest = Site()
        newSiteDest.makeAddress(destAddr)
        self.destSite = newSiteDest
    
    def setSiteFloors(self, srcFloors, destFloors):
        self.beginSite.setFloorNum(int(srcFloors))
        self.destSite.setFloorNum(int(destFloors))
    
    def setSiteIsResidental(self, srcResidental, destResidental):
        self.beginSite.setResidentalStatus(bool(srcResidental))
        self.destSite.setResidentalStatus(bool(destResidental))
    
    def setNumOfVehicles(self, numOfvehicles):
        self.movementTeam.setVehicles(numOfvehicles.split())
        
    def setNumOfWorkers(self, num):
        self.movementTeam.setWorkers(int(num))
    
    def setHeavyStuff(self, HeavyStuffIDs):
        self.heavyStuffIds = HeavyStuffIDs.split()

    def calculateCost(self):
        self.insurance.setValidationTime(self.startDate, self.endDate)
        insuranceCost = self.insurance.getCost()
        vehicleCost = sum([self.movementTeam.vehicleCatalog.getVehicleById(vehicleID).cost for vehicleID in self.movementTeam.vehicles])
        workerCost = sum([self.movementTeam.employeeCatalog.getWorkerByID(workerID).salary for workerID in self.movementTeam.workers])
        heavyStuffCost = len(self.heavyStuffIds) * 20
        totalFloorsCost = (self.beginSite.floorNum + self.destSite.floorNum) * 20
        cityCost = 0
        if self.beginSite.address.city != self.destSite.address.city:
            cityCost = 400
        self.totalCost = insuranceCost + vehicleCost + workerCost + heavyStuffCost + totalFloorsCost + cityCost
        self.payment.setCost(self.totalCost)
        