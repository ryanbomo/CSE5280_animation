#Python Animation 
#Author: Ryan Bomalaski
#Date: 03/19/2018

from ball import Ball
from obstacle import Obstacle
from vpython import *
        
        
## Create list of balls, using origin Vector and goal coordinates    
red_balls_info = [[vector(6,1,0),[-7,1]],
             [vector(6,0,0),[-7,0]],
             [vector(6,-1,0),[-7,-1]],
             [vector(7,1,0),[-6,1]],
             [vector(7,0,0),[-6,0]],
             [vector(7,-1,0),[-6,-1]]]
green_balls_info = [[vector(1,7,0),[1,-6]],
               [vector(0,7,0),[0,-6]],
               [vector(-1,7,0),[-1,-6]],
               [vector(1,6,0),[1,-7]],
               [vector(0,6,0),[0,-7]],
               [vector(-1,6,0),[-1,-7]]]
cyan_balls_info = [[vector(1,-7,0),[1,6]],
              [vector(0,-7,0),[0,6]],
              [vector(-1,-7,0),[-1,6]],
              [vector(1,-6,0),[1,7]],
              [vector(0,-6,0),[0,7]],
              [vector(-1,-6,0),[-1,7]]]
blue_balls_info = [[vector(-6,1,0), [7,1]],
              [vector(-6,0,0), [7,0]],
              [vector(-6,-1,0), [7,-1]],
              [vector(-7,1,0),[6,1]],
              [vector(-7,0,0),[6,0]],
              [vector(-7,-1,0),[6,-1]]]

## Create list of ball objects
blue_balls = []
red_balls = []
green_balls = []
cyan_balls = []

## Populate list of ball objects
for i in blue_balls_info:
    blue_balls.append(Ball(i[0],0.1,color.blue,i[1]))
    
for i in green_balls_info:
    green_balls.append(Ball(i[0],0.1,color.green,i[1]))

for i in red_balls_info:
    red_balls.append(Ball(i[0],0.1,color.red,i[1]))

for i in cyan_balls_info:
    cyan_balls.append(Ball(i[0],0.1,color.cyan,i[1]))

list_of_objects = list()
list_of_balls = list()

for i in blue_balls:
    list_of_balls.append(i)
for i in green_balls:
    list_of_balls.append(i)
for i in red_balls:
    list_of_balls.append(i)
for i in cyan_balls:
    list_of_balls.append(i)
    
for i in list_of_balls:
    list_of_objects.append(i)

obstacles = [Obstacle(0,0),
             Obstacle(1.5,1.5),
             Obstacle(-1.5,-1.5),
             Obstacle(1.5,-1.5),
             Obstacle(-1.5,1.5)]


for i in obstacles:
    list_of_objects.append(i)

while True:
    for i in range(len(list_of_balls)):
        list_left = list_of_objects[0:i]
        list_right = list_of_objects[i+1:len(list_of_objects)]
        list_whole = list_left + list_right
        list_of_balls[i].update_objects(list_whole)
        list_of_balls[i].descend_gradient()
        list_of_objects[i] = list_of_balls[i]
        
