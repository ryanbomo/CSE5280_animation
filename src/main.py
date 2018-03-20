#Python Animation 
#Author: Ryan Bomalaski
#Date: 03/19/2018

from board import *
        
def main():
    board = Board(10,10)
    coords = [[[1,1],[3,5]],
              [[2,2],[5,8]]]
    for i in coords:
        board.createPoint(i[0],i[1])
    for i in board.points:
        print(i.getLocation())
        
main()