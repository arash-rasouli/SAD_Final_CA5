from random import sample

TEST_NUM = 20

class Employee:
    def __init__(self, employeeId, name, salary, workTime):
        self.employeeId = employeeId
        self.name = name
        self.salary = salary
        self.workTime = workTime
        self.isBusy = False 

class Driver(Employee):
    def __init__(self, employeeId, name, salary, workTime, vehicleId):
        super().__init__(employeeId, name, salary, workTime)
        self.vehicleId = vehicleId


class Worker(Employee):
    def __init__(self, employeeId, name, salary, workTime, age, skills):
        super().__init__(employeeId, name, salary, workTime)
        self.skills = skills
        self.age = age

class Skill:
    def __init__(self, skillId, title, Description):
        self.skillId = skillId
        self.title = title
        self.Description = Description

class EmployeeCatalog:
    def __init__(self):
        self.numOfEmployees = 0
        self.availableWorkers = 0 
        self.availableDrivers = 0
        self.workers = []
        self.drivers = []
        self.initiateDrivers()
        self.initiateWorkers()
        
    def initiateWorkers(self):
        skills = []
        for i in range(TEST_NUM):
            skills.append(Skill(i, "skill_" + str(i), "skill_description_" + str(i)))
        
        for i in range(TEST_NUM):
            newWorker = Worker(self.numOfEmployees, "worker_" + str(i), 150, ["m", "t", "w", "th", "f"], 20, sample(skills, 2))
            self.numOfEmployees += 1
            self.workers.append(newWorker)
        self.availableWorkers = TEST_NUM

    def initiateDrivers(self):
        for i in range(TEST_NUM):
            newDriver = Driver(self.numOfEmployees, "driver_" + str(i), 150, ["m", "t", "w", "th", "f"], i)
            self.numOfEmployees += 1
            self.drivers.append(newDriver)
        self.availableDrivers = TEST_NUM
    
    def getWorkers(self, num):
        if (self.availableWorkers < num):
            print("Not Enough workers")
            return
        selectedWorkers = []
        for i in self.workers:
            if (len(selectedWorkers) == num):
                break
            if (i.isBusy):
                continue
            selectedWorkers.append(i.employeeId)
        self.updateAvailableWorkers(selectedWorkers)
        return selectedWorkers

    def getWorkerByID(self, _id):
        for worker in self.workers:
            if worker.employeeId == _id:
                return worker
            
    def updateAvailableWorkers(self, listOfWorkers):
        for i in listOfWorkers:
            for j in self.workers:
                if (j.employeeId == i):
                    j.isBusy = True
        
