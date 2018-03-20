#Python Animation 
#Author: Ryan Bomalaski
#Date: 03/19/2018

from board import *
from vpython import *
import copy

class Ball:
    def __init__(self, vect, rad, col,dest_coordinates):
        self.vector = vect
        #self.arrow_vect = copy.copy(vect)
        self.color = col
        self.radius = rad
        self.destination = dest_coordinates
        self.vpython_object = sphere(pos=self.vector, radius=self.radius, color=self.color)
       # self.arrow = arrow(pos=self.vpython_object.pos, axis=self.arrow_vect, color=color.yellow)
        
    def move(self,d_X, d_Y):
        # Update X and Y
        self.vector.x += d_X
        self.vector.y += d_Y
        
        # Update Arrow X and Y
        #self.arrow_vect.x = 10*d_X
        #self.arrow_vect.y = 10*d_Y
        
        # Update vpython Objects
        self.vpython_object.pos = self.vector
        #self.arrow.pos = self.vector
        #self.arrow.axis = self.arrow_vect
        
    def step_to_destination(self):
        print("Fart")
        
        
        
red_balls_info = [[vector(9,1,0),[-10,1]],
             [vector(9,0,0),[-10,0]],
             [vector(9,-1,0),[-10,-1]],
             [vector(10,1,0),[-9,1]],
             [vector(10,0,0),[-9,0]],
             [vector(10,-1,0),[-9,-1]]]
green_balls_info = [[vector(1,10,0),[1,-9]],
               [vector(0,10,0),[0,-9]],
               [vector(-1,10,0),[-1,-9]],
               [vector(1,9,0),[1,-10]],
               [vector(0,9,0),[0,-10]],
               [vector(-1,9,0),[-1,-10]]]
cyan_balls_info = [[vector(1,-10,0),[1,9]],
              [vector(0,-10,0),[0,9]],
              [vector(-1,-10,0),[-1,9]],
              [vector(1,-9,0),[1,10]],
              [vector(0,-9,0),[0,10]],
              [vector(-1,-9,0),[-1,10]]]
blue_balls_info = [[vector(-9,1,0), [10,1]],
              [vector(-9,0,0), [10,0]],
              [vector(-9,-1,0), [10,-1]],
              [vector(-10,1,0),[9,1]],
              [vector(-10,0,0),[9,0]],
              [vector(-10,-1,0),[9,-1]]]

blue_balls = []
red_balls = []
green_balls = []
cyan_balls = []

for i in blue_balls_info:
    blue_balls.append(Ball(i[0],0.1,color.blue,i[1]))
    
for i in green_balls_info:
    green_balls.append(Ball(i[0],0.1,color.green,i[1]))

for i in red_balls_info:
    red_balls.append(Ball(i[0],0.1,color.red,i[1]))

for i in cyan_balls_info:
    cyan_balls.append(Ball(i[0],0.1,color.cyan,i[1]))
