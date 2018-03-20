
from vpython import *

class Obstacle:
    def __init__(self, x,y):
        self.field_radius = 1
        self.x = x
        self.y = y
        self.rod = cylinder(pos=vector(self.x, self.y,0), axis=vector(0,0,1), radius = 1)
        
    
    def get_X(self):
        return self.x
    
    def get_Y(self):
        return self.y