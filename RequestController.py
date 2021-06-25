from user import *
from movementReq import *
from heavyStuff import *
from employee import *
from DAO import *

class RequestController:
    def __init__(self):
        self.loginUserId = 0
        self.requests = []
        self.heavyStuffCatalog = HeavyStuffCatalog()
        self.EmployeeCatalog = EmployeeCatalog()
        self.payments = []
        self.dao = DAO()
        self.numOfRequests = self.dao.getLastId()

    def setUserLoginId(self, userid):
        self.loginUserId = userid
        
    def makeNewMovementReq(self, beginAddr, destAddr, beginFloors, endFloors, beginResidental, endResidental,
                          heavyStuff, numOfVehicles, numOfWorkers, startDate, endDate):
        payment = Payment(self.numOfRequests)
        self.payments.append(payment)
        newMovementReq = MovementReq(self.numOfRequests, self.loginUserId, self.heavyStuffCatalog, self.EmployeeCatalog, payment)
        
        newMovementReq.makeSites(beginAddr, destAddr)
        newMovementReq.setSiteFloors(beginFloors, endFloors)
        newMovementReq.setSiteIsResidental(beginResidental, endResidental)
        newMovementReq.setHeavyStuff(heavyStuff)
        newMovementReq.setNumOfVehicles(numOfVehicles)
        newMovementReq.setNumOfWorkers(numOfWorkers)
        newMovementReq.setDateTimes(startDate, endDate)
        newMovementReq.calculateCost()
        
        self.requests.append(newMovementReq)
        self.numOfRequests += 1
        
        self.dao.saveRequest(newMovementReq)
