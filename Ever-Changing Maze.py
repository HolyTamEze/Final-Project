# This is currently a work in progress.

import random

def MazeCreator(rows):
    wall = "W"
    pieces = ["W", "S"]
    
    for i in range(1, rows + 1):
        for j in range(i, rows + 1):
            print(wall, end = ' ')
        for k in range(1, i):
            print(random.choice(pieces), end = ' ')
        print()
    return ""
    
    
            
    

print(MazeCreator(int(input("Enter a number for the rows: "))))

