class Obstacle:
    
    
    def __init__(self, locCoords):
        self.location = locCoords
        

    def getLocation(self):
        return self.location
    
    def setLocation(self,newX, newY):
        self.location = [newX, newY]
        return self.location