HEAVY_STUFF = ["piano", "yakhchal", "gaz", "komod", "bufe", "mobl", "takht"]

class HeavyStuff:
    def __init__(self, heavyStuffId, name):
        self.heavyStuffId = heavyStuffId
        self.name = name

class HeavyStuffCatalog:
    def __init__(self):
        self.heavyStuff = []
        self.initiateStuffCatalogs()
        
    def initiateStuffCatalogs(self):
        for i in range(len(HEAVY_STUFF)):
            self.heavyStuff.append(HeavyStuff(i, HEAVY_STUFF[i]))

    def getAllStuff(self):
        return self.heavyStuff
    
    def getHeavyStuff(self, heavyStuffId):
        for i in self.heavyStuff:
            if (i.heavyStuffId == heavyStuffId):
                return i