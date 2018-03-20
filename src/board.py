from point import *
from obstacle import *

class Board:
    points = []
    obstacles = []
    
    def __init__(self,sizeX, sizeY):
        self.dimX = sizeX
        self.dimY = sizeY
        
    def createPoint(self,locsCoords, destCoords):
        if locsCoords[0]>self.dimX or locsCoords[1]>self.dimY or destCoords[0]>self.dimX or destCoords[1]>self.dimY:
            return 0
        self.points.append(Point(locsCoords,destCoords))
        return 1
    
    def createObstacles(self,locsCoords):
        if locsCoords[0]>self.dimX or locsCoords[1]>self.dimY:
            return 0
        self.obstacles.append(Obstacle(locsCoords))
        return 1