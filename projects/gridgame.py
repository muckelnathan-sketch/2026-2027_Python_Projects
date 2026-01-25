position = [2, 3]  # must be inside the 5x5 grid
import os
running = True # creating a universal variable so if the player dies then we can end the game
def game_map():
    for y in range(10): #running through every row
        for x in range(10): #running through every column
            if [y, x] == position: #if the position is where the player is then print the X
                print("X", end=" ")
            else: #otherwise print the circle
                print("o", end=" ")
        print()  # new line after each row
def c(works):
    if not works: #efficient function to be called to print the same thing instead of a bunch of print statements
        print("you cant move there")
game_map() #call the game map at the beginning of the game
def game(): #this is the control of the game
    works=True
    global position
    print("DEBUG:", position)
    where = input("where: ")
    match where:
        case "w":
            if position[0] > 0:position[0] -= 1 
            else:works = False
        case "s": #copilot said this is more efficient
            if position[0] < 9:position[0] += 1 
            else:works = False
        case "a":
            if position[1] > 0:position[1] -= 1 
            else:works = False
        case "d":
            if position[1] < 9:position[1] += 1
            else:works = False

    c(works) 
while running: 
    os.system('cls')
    game_map()
    game()

    #some reason the program gets confused when X is on the corners and top , it was because my window of view of the code would go up a row when it printed "u cant go there"
    #tmr i will add some gameplay features like characters at certain locations or even create a random maze