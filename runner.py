#! python3
import random
import os
#Here's what we have to do.

#Have a class that defines the x and y of the player.

#Create a move function inside the object.

#once the control is given, check if it breaks the array.

#if it doesn't, then check if it is riding on the forbidden area.

#only if it passes these tests, change the location of the character

#Todo: Build a fucking class.

def cls():
    try:
        os.system('cls')
    except RuntimeError:
        os.system('clear')

class Peep:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self,ky):
        if(ky=='w'):
            self.y-=1
        if(ky=='a'):
            self.x-=1
        if(ky=='s'):
            self.y+=1
        if(ky=='d'):
            self.x+=1
        else:
            print("Illegal input. Cannot move character.")
#mark a random position in the fucking maze.


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

def isEmpty(x,y):
    if(MAZE[x][y]=='#'):
        return False
    else:
        return True
iX = 0
iY = 0
while True:
    iX = random.randint(0,37)
    iY = random.randint(0,23)
    if isEmpty(iX,iY):
        break
    else:
        continue

p = Peep(iX,iY)

#Yay, everything is set up.
#Now, you need to:
#   print the maze and the prompt
#   flush the screen every single time the control is updated.
#   every time the X moves, clear the current position, and then put the new guy in the new position

