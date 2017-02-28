#! python3
import random
import os

#Function to clear the screen
def cls():
    try:
        os.system('cls')
    except RuntimeError:
        os.system('clear')

#Player object
class Peep:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self,ky):
        if(ky=='w'):
            self.y-=1
        elif(ky=='a'):
            self.x-=1
        elif(ky=='s'):
            self.y+=1
        elif(ky=='d'):
            self.x+=1
        else:
            print("Illegal input. Cannot move character.")
#Maze 2-D list object
MAZE = [list("#####################################"),
        list("# #       #       #     #         # #"),
        list("# # ##### # ### ##### ### ### ### # #"),
        list("#       #   # #     #     # # #   # #"),
        list("##### # ##### ##### ### # # # ##### #"),
        list("#   # #       #     # # # # #     # #"),
        list("# # ####### # # ##### ### # ##### # #"),
        list("# #       # # #   #     #     #   # #"),
        list("# ####### ### ### # ### ##### # ### #"),
        list("#     #   # #   # #   #     # #     #"),
        list("# ### ### # ### # ##### # # # #######"),
        list("#   #   # # #   #   #   # # #   #   #"),
        list("####### # # # ##### # ### # ### ### #"),
        list("#     # #     #   # #   # #   #     #"),
        list("# ### # ##### ### # ### ### ####### #"),
        list("# #   #     #     #   # # #       # #"),
        list("# # ##### # ### ##### # # ####### # #"),
        list("# #     # # # # #     #       # #   #"),
        list("# ##### # # # ### ##### ##### # #####"),
        list("# #   # # #     #     # #   #       #"),
        list("# # ### ### ### ##### ### # ##### # #"),
        list("# #         #     #       #       # #"),
        list("# ###################################")]
#Function to check if the particular element in the list is empty.
def isEmpty(x,y):
    # y and x are switched because that's how lists work.
    if(MAZE[y][x]=='#'):
        return False
    else:
        return True
#inital coordinates of the player
iX = 0
iY = 0
while True:
    #creates a random coordinate
    iX = random.randint(0,36)
    iY = random.randint(0,22)
    if isEmpty(iX,iY): #checks if its empty first
        break
    else:
        continue
#initializing the Player object
p = Peep(iX,iY)

#Function to insert the player into the Maze
def insG(X,Y):
    MAZE[Y][X] = " " #clears the last known position
    MAZE[p.y][p.x] = "X"

#function to print out the 2D list
def printMaze():
    for i in MAZE:
        for j in i:
            print(j,end='')
        print()
#variable that stores the key pressed by the player
control = ""
#inserting the player into the maze
insG(p.x,p.y)
#the gameplay
while(control != "quit"):
    cls() #clears the terminal to give a pseudo-GUI feel.
    printMaze() #prints the maze with the player in it.
    control=input("enter command:[w,a,s,d,quit]  ")
    X = p.x#storing the old coordinates for clearing the path
    Y = p.y#and as a fallback incase it was an invalid move
    p.move(control)
    #checks for invalid move.
    if not isEmpty(p.x,p.y):
        p.x = X
        p.y = Y
        print("INVALID MOVE")
    #changes the position of the player
    insG(X,Y)


