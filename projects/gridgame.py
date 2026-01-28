import os
import random #importing valuable libraries
diologue = ["Careful where you step… the monsters here don’t roar. They giggle. Honestly, it’s worse.","The maze watches you, you know. Not in a creepy way. More like a disappointed parent.","If you hear scratching behind the walls, don’t panic. It’s probably just the wall trying to get comfortable.","Monsters roam these halls, but don’t worry — most of them are terrible at directions.","Treasure is everywhere! The maze practically throws it at you. Suspiciously generous, if you ask me.","Some say the maze shifts to protect you. Others say it shifts to trap you. Either way, it’s shifting.","If a monster starts chasing you, just run in circles. They get dizzy easily.","The maze has eyes. Not literal ones… I think. Actually, don’t quote me on that.","I once found a chest filled with gold. Then another filled with socks. The maze has a sense of humor.","Monsters here aren’t all bad. One tried to scare me yesterday but apologized afterward.","If the walls start humming, that means treasure is nearby… or a monster is snoring. Good luck.","The maze remembers every step you take. It just pretends it doesn’t.","Treasure piles up because the monsters keep forgetting where they put it.","If you feel like you’re being watched, relax — the maze just likes your vibe.","Some monsters guard treasure. Others guard snacks. Honestly, the snack ones are more dangerous.","The maze isn’t evil. It’s just… mischievous. Like a cat that’s also a building.","I swear the walls move when I’m not looking. Last week one tried to high‑five me.","There’s treasure everywhere, but the real treasure is not getting eaten. Probably.","The monsters here are scary until you realize they’re just as lost as you are.","If you hear laughter echoing through the halls, don’t worry — that’s just the maze enjoying the show."]
player_icon = "\x1b[34mX\x1b[0m"
chest_icon = "\x1b[38;5;220m¤\x1b[0m"
wall_icon = "\x1b[31m█\x1b[0m" #color ansi codes for themed objects
NPC_icon = "\x1b[32mX\x1b[0m"
walls = [] 
chests = [] #arrays full of the coordinates for objects and entities
player = [2, 3]
NPCs = []
chest_opening = False
need_diologue = False #these are triggered off and on for the print_statements later
being_said = None
running = True # creating a universal variable so if the player dies then we can end the game



def check_npc_collision(npc:list[int,bool]) -> bool:
    global need_diologue
    global being_said
    dy = abs(npc[0] - player[0])
    dx = abs(npc[1] - player[1])
    if dy <= 1 and dx <= 1:
        need_diologue = True
        being_said = npc[3]
    return dy <= 2 and dx <= 2  



def NPC():
    global npc
    global need_diologue
    global being_said
    need_diologue = False
    being_said = None
    collision_checker = lambda ghost: (
    ghost[:2] not in walls
    and ghost[:2] not in chests
    and ghost[0] != 0
    and ghost[0] != 10
    and ghost[1] != 0
    and ghost[1] != 49
)
    for npc in NPCs:
        if check_npc_collision(npc):
            npc[2] = True
        else:
            npc[2] = False
        while True:
            if npc[2]:
                break
            vector = random.choice([0,1]) #Y and X
            direction = random.choice(["+","-"])
            if direction == "-":
                npc_ghost = npc.copy()
                npc_ghost[vector]-=1
                if collision_checker(npc_ghost) and not npc[2]:
                    npc[vector] -= 1
                    break
            else:
                npc_ghost = npc.copy()
                npc_ghost[vector] += 1

                if collision_checker(npc_ghost) and not npc[2]:
                    npc[vector] += 1
                    break
            break


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
        while True:
            wall_coordinates = [random.randint(1,10),random.randint(1,50)]
            if collision_check(wall_coordinates):
                walls.append(wall_coordinates)
                break

def NPC_spawning(amount=1):
    for _ in range(amount):
        while True:
            npc_coordinates = [random.randint(1,10),random.randint(1,50), True, random.choice(diologue)]
            if collision_check(npc_coordinates):
                NPCs.append(npc_coordinates)
                break


def chest_gen(amount = 5):
    for _ in range(amount):
        while True:
            chest_coordinates = [random.randint(1,10),random.randint(1,50)]
            if collision_check(chest_coordinates):
                chests.append(chest_coordinates)
                break
collision_check = lambda l: True if l not in walls and l != player and l not in chests else None


def entrapment_debugger(target:list[int]):
    for i in range(2):
        if i == 1:
            _min = 1;_max = 10
        else:
            _min = 1;_max = 49
            ghost = target.copy()
            ghost[i]+=1
            if ghost in walls or ghost[i] > _max: #used a lil co pilot, this system is complex
                ghost = target.copy()
                ghost[i]-=1
                if ghost in walls or ghost[i] < _min:
                    continue
            return True
    else:
        i = random.randint(0,1)
        ghost = target.copy()
        ghost[i] -= 1
        if ghost in walls:
            walls.remove(ghost)


def win():
    global running
    if len(chests) <= 0:
        os.system('cls')
        print("YOU WIN")
        running = False
        return True
    else:
        return False

def chest_open(position):
    global chest_opening
    chests.pop(chests.index(position))
    chest_opening = True
    
    
maze_gen(150)
chest_gen(10)
NPC_spawning(2)
entrapment_debugger(player)
for chest in chests:
    entrapment_debugger(chest)



def game_map():
    for y in range(10): #running through every row
        for x in range(50): #running through every column
            if (current := [y,x]) == player or current in walls or current in chests or current in [npc[:2] for npc in NPCs]:
                if current == player: #if the position is where the player is then print the X
                    print(player_icon, end=" ")
                elif current in walls:
                    print(wall_icon, end=" ")
                elif current in chests:
                    print(chest_icon, end = " ")
                elif current in [npc[:2] for npc in NPCs]:
                    print(NPC_icon, end=" ")
            else: #otherwise print the circle
                print(" ", end=" ")
        print()  # new line after each row

def print_statement(works, chest_opened = False):
    if not works:
        print("you can't move there")
    elif chest_opened:
        print("you've found treasure!!!")
    if need_diologue:
        print(being_said)
    if works and not chest_opened and not need_diologue:
        print()

game_map() #call the game map at the beginning of the game
def game(): #this is the control of the game
    if not win():
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
        NPC()
        os.system('cls')
        print_statement(works, chest_opening) 
        chest_opening = False
while running: 
    game_map()
    game()

    #TODAY IM ADDING A SYSTEM TO MAKE SURE WALLS,CHESTS DONT SPAWN ON OTHER ENTITIES, AND NPC'S!!