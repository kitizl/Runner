#! python3

#Here's what we have to do.

#Have a class that defines the x and y of the player.

#Create a move function inside the object.

#once the control is given, check if it breaks the array.

#if it doesn't, then check if it is riding on the forbidden area.

#only if it passes these tests, change the location of the character

#Todo: Build a fucking class.

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



