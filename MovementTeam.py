from vehicle import *
from employee import *

class MovementTeam:
    def __init__(self, EmployeeCatalogInstance):
        self.vehicles = []
        self.drivers = []
        self.workers = []
        self.employeeCatalog = EmployeeCatalogInstance
        self.vehicleCatalog = VehicleCatalog(self.employeeCatalog)
                
    def setVehicles(self, numOfVehiclesList):
       self.vehicles = self.vehicleCatalog.getVehicles(numOfVehiclesList)
       self.setDrivers()
       
    def setWorkers(self, num):
        self.workers = self.employeeCatalog.getWorkers(num)
    
    def setDrivers(self):
        for vehicle in self.vehicles:
            driverId = self.vehicleCatalog.getVehicleById(vehicle)
            self.drivers.append(driverId)
