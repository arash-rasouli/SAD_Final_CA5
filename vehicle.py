from random import sample
TEST_NUM = 20

VEHICLE_TYPES = ["vanet", "neysan", "kamiyun"]
VEHICLE_COST = [200, 300, 400]
class Vehicle:
    def __init__(self, vehicleId, driverId, vehicleType, model, name):
        self.vehicleId = vehicleId
        self.driverId = driverId
        self.vehicleType = vehicleType
        self.model = model
        self.name = name
        self.isBusy = False
        self.cost = VEHICLE_COST[VEHICLE_TYPES.index(vehicleType)]
         
class VehicleCatalog:
    def __init__(self, employeeCatalog):
        self.vehicles = []
        self.numOfVehicles = 0
        self.employeeCatalog = employeeCatalog
        self.availableVehicles = [0, 0, 0]
        self.initiateVehicles()
        
    def initiateVehicles(self):
        for i in range(TEST_NUM):
            newVehicle = Vehicle(i, str(self.employeeCatalog.drivers[i]), sample(VEHICLE_TYPES, 1)[0], "model_" + str(i), "name_" + str(i))
            self.numOfVehicles += 1
            self.vehicles.append(newVehicle)
            self.availableVehicles[VEHICLE_TYPES.index(newVehicle.vehicleType)] += 1

    def getVehicles(self, numOfVehiclesList):
        selectedVehicles = []
        for i in range(3):
            if (self.availableVehicles[i] < int(numOfVehiclesList[i])):
                print("Not Enough vehicles of type ", VEHICLE_TYPES[i])
                return
            for j in range(int(numOfVehiclesList[i])):
                for vehicle in self.vehicles:
                    if (vehicle.isBusy):
                        continue
                    if vehicle.vehicleType == VEHICLE_TYPES[i] and vehicle.vehicleId not in selectedVehicles:
                        selectedVehicles.append(vehicle.vehicleId)
                        break
        self.updateAvailableVehicles(selectedVehicles)
        return selectedVehicles
    
    def getVehicleById(self, _id):
        for v in self.vehicles:
            if v.vehicleId == _id:
                return v
    
    def updateAvailableVehicles(self, listOfVehicles):
        for i in listOfVehicles:
            for j in self.vehicles:
                if (j.vehicleId == i):
                    j.isBusy = True
