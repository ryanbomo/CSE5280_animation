#Python Animation 
#Author: Ryan Bomalaski
#Date: 03/19/2018

from board import *
from ball import Ball
from obstacle import Obstacle
from vpython import *
        
        
## Create list of balls, using origin Vector and goal coordinates    
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


obstacle1 = Obstacle(-2,-2)
obstacle2 = Obstacle(2,-2)
obstacle3 = Obstacle(-2,2)
obstacle4 = Obstacle(2,2)
    
list_of_objects.append(obstacle1)
list_of_objects.append(obstacle2)
list_of_objects.append(obstacle3)
list_of_objects.append(obstacle4)

while True:
    for i in range(len(list_of_balls)):
        list_left = list_of_objects[0:i]
        list_right = list_of_objects[i+1:len(list_of_objects)]
        list_whole = list_left + list_right
        list_of_balls[i].update_objects(list_whole)
        list_of_balls[i].descend_gradient()
        list_of_objects[i] = list_of_balls[i]
        