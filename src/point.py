class Point:
    
    
    def __init__(self, locCoords, targetCoords):
        self.location = locCoords
        self.destination = targetCoords
        

    def getLocation(self):
        return self.location
    
    def getDestination(self):
        return self.destination
    
    def setLocation(self,newX, newY):
        self.location = [newX, newY]
        return self.location
    
    def setDestination(self,newX, newY):
        self.destination = [newX, newY]
        return self.destination