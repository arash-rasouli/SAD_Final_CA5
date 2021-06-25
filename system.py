from RequestController import *
class System:
    def __init__(self):
        self.arguments = []
        self.requestController = RequestController()
        self.Users = [['Sina', '1234'], ['Amirhossein', '1234'], ['Arash', '1234']]
        
    def loginUser(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if [username, password] not in self.Users:
            print("Wrong username or password")
            self.loginUser()
        else:
            userID = self.Users.index([username, password])
            self.requestController.setUserLoginId(userID)
            print("You have logged in successfully")
        
    def run(self):
        self.loginUser()
        req = input("options:\n 1.movement request\n")
        print("Enter begin and end addresses(example: city/region/street/alley/number)")
        beginAddr = input("From: ")
        destAddr = input("To: ")
        
        print("Enter begin and end floors(example: number of floors)")
        beginFloors = input("Begin floors: ")
        endFloors = input("End floors: ")
        
        print("Enter begin and end residental status(example: True/False)")
        beginResidental = input("Begin residental status: ")
        endResidental= input("End residental status: ")
        
        print("Choose heavy stuff ids from list below(example: 1 2 3)")
        self.print_heavyStuff_list()
        heavyStuff = input()
        
        print("Enter number of vehicles you need for each type of vehicle(example: 0 0 2)")
        numOfVehicles = input("vanet, neysan, kamiyun: ")

        print("Enter number of workers you need(example: 4)")
        numOfWorkers = input("needed workers: ")

        print("Enter start and end dates(example: year/month/day/hour)")
        startDate = input("start date: ")
        endDate = input("end date: ")
        
        if int(req) == 1:
            self.requestController.makeNewMovementReq(beginAddr, destAddr, beginFloors, endFloors, 
                        beginResidental, endResidental, heavyStuff, numOfVehicles, numOfWorkers, startDate, endDate)
    
    def print_heavyStuff_list(self):
        ans = " " 
        AllHeavyStuff = self.requestController.heavyStuffCatalog.getAllStuff()
        for heavyStuff in AllHeavyStuff:
            ans += str(heavyStuff.heavyStuffId) + "." + heavyStuff.name + " "
        print(ans)

system = System()
while 1:
    system.run()