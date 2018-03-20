#Python Animation 
#Author: Ryan Bomalaski
#Date: 03/19/2018

from board import *
from vpython import *

sphere(pos = vector(-1,0,0), radius = 0.5, color = color.green)
arrow(pos=vector(-1,0,0), color = color.red)
        
def main():
    board = Board(10,10)
    coords = [[[1,1],[3,5]],
              [[2,2],[5,8]]]
    for i in coords:
        board.createPoint(i[0],i[1])
    for i in board.points:
        print(i.getLocation())
        
main()