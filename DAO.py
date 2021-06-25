import csv
import os.path
from datetime import *
from movementReq import *
from Payment import *
from site import *
from MovementTeam import *
  
FILE_ADDRESS = "movementReqFile.csv"

class DAO:
    def __init__(self):
        self.fields = ["RequestID","UserID","InsuranceID","TotalCost","StartDate","EndDate","BeginSite","DestSite","MovementTeam","HeavyStuffIDs","Payment"]
        if (not os.path.isfile("movementReqFile.csv")):
            with open(FILE_ADDRESS, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(self.fields)

    def _getAddressString_(self, address):
        ans = str(address.city) + "/"
        ans += str(address.region) + "/"
        ans += str(address.street) + "/"
        ans += str(address.alley) + "/"
        ans += str(address.number)
        return ans

    def _getSiteString_(self, site):
        ans = "{"
        ans += "FloorNum: " + str(site.floorNum) + " # "
        ans += "IsResidential: " + str(site.isResidential) + " # "
        ans += "Address: " + str(self._getAddressString_(site.address)) + "}"
        return ans
    
    def _getMovementTeamString_(self, movementTeam):
        ans = "{"
        ans += "Vehicles: [" + "-".join(list(map(str, movementTeam.vehicles))) + "] # "
        ans += "Workers: [" + "-".join(list(map(str, movementTeam.workers))) + "]}"
        return ans

    def _getHeavyStuffIDsString_(self, heavyStuffIDs):
        ans = "[" + "-".join(list(map(str, heavyStuffIDs))) + "]"
        return ans

    def _getPaymentString_(self, payment):
        ans = "{"
        ans += "Id: "+ str(payment.id) + " # "
        ans += "Cost: "+ str(payment.cost) + " # "
        ans += "Paid: "+ str(payment.paid) + " # "
        ans += "Deposit: "+ str(payment.deposit) + "}"
        return ans

    def saveRequest(self, request):
        row = []

        row.append(str(request.requestId))
        row.append(str(request.userId))
        row.append(str(request.requestId))
        row.append(str(request.totalCost))
        row.append(str(request.startDate))
        row.append(str(request.endDate))
        row.append(str(self._getSiteString_(request.beginSite)))
        row.append(str(self._getSiteString_(request.destSite)))
        row.append(str(self._getMovementTeamString_(request.movementTeam)))
        row.append(str(self._getHeavyStuffIDsString_(request.heavyStuffIds)))
        row.append(str(self._getPaymentString_(request.payment)))

        with open(FILE_ADDRESS, 'a', newline='') as csvfile:
            csvAppender = csv.writer(csvfile)
            csvAppender.writerow(row)

    def showRequest(self, requestId):
        header = []
        rows = []
        with open(FILE_ADDRESS, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            header = next(csvreader)
            for row in csvreader:
                rows.append(row)
        
        founded = None

        for i in rows:
            if(i[0] == str(requestId)):
                founded = i
                break
        
        if(founded != None):
            for i in range(len(self.fields)):
                print(self.fields[i] + " : " + founded[i])
    
    def getFieldOfRequest(self, requestId, filedName):
        header = []
        rows = []
        with open(FILE_ADDRESS, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            header = next(csvreader)
            for row in csvreader:
                rows.append(row)
        
        founded = None

        for i in rows:
            if(i[0] == str(requestId)):
                founded = i
                break
        
        if(founded != None):
            for i in range(len(self.fields)):
                if (self.fields[i] == filedName):
                    return founded[i]
                
    def getLastId(self):
        header = []
        rows = []
        with open(FILE_ADDRESS, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            header = next(csvreader)
            for row in csvreader:
                rows.append(row)
        if len(rows) == 0:
            return 0
        return int(rows[-1][0])