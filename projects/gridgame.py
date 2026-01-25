import os
import random
walls = []
chests = []
player = [2, 3]
chest_opening = False
def obstacle_checker(vector_position):
    def func(sim_position):
        if sim_position in walls:return False
        if sim_position in chests: chest_open(sim_position)
        return True
    sim_position = player.copy()
    match vector_position:
        case 'down':
            sim_position[0] += 1
            return func(sim_position)
        case 'up':
            sim_position[0] -= 1
            return func(sim_position)
        case 'left':
            sim_position[1] -= 1
            return func(sim_position)
        case 'right':
            sim_position[1] += 1
            return func(sim_position)
def maze_gen(amount = random.randint(10,30)):
    for _ in range(amount):
        walls.append([random.randint(1,10),random.randint(1,50)])

def chest_gen(amount = 5):
    for _ in range(amount):
        chests.append([random.randint(1,10),random.randint(1,50)])

def chest_open(position):
    global chest_opening
    chests.pop(chests.index(position))
    chest_opening = True
    
maze_gen(100)
chest_gen(10)
running = True # creating a universal variable so if the player dies then we can end the game
def game_map():
    for y in range(10): #running through every row
        for x in range(50): #running through every column
            if (current := [y,x]) == player or current in walls or current in chests:
                if current == player: #if the position is where the player is then print the X
                    print("X", end=" ")
                elif current in walls:
                    print("█", end=" ")
                elif current in chests:
                    print("¤", end = " ")
            else: #otherwise print the circle
                print(" ", end=" ")
        print()  # new line after each row

def print_statement(works, chest_opened = False):
    if not works:
        print("you can't move there")
    elif chest_opened:
        print("you've found treasure!!!")

game_map() #call the game map at the beginning of the game
def game(): #this is the control of the game
    works=True
    global player
    global chest_opening
    #print("DEBUG:", player)
    match input("where: ").lower().strip():
        case "w":
            if player[0] > 0 and obstacle_checker('up'):player[0] -= 1
            else:works = False
        case "s": #copilot said this is more efficient
            if player[0] < 9 and obstacle_checker('down'):player[0] += 1 
            else:works = False
        case "a":
            if player[1] > 0 and obstacle_checker('left'):player[1] -= 1
            else:works = False
        case "d":
            if player[1] < 49 and obstacle_checker("right"):player[1] += 1 
            else:works = False
    os.system('cls')
    print_statement(works, chest_opening) 
    chest_opening = False
while running: 
    game_map()
    game()