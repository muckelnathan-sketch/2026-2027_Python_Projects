position = [2, 3]  # must be inside the 5x5 grid
import os
def game_map():
    for y in range(5):
        for x in range(5):
            if [y, x] == position:
                print("X", end=" ")
            else:
                print("o", end=" ")
        print()  # new line after each row
def c(works):
    if not works:
        print("you cant move there")
game_map()
def game():
    work=True
    global position
    where = input("where: ")
    match where:
        case "w": 
            if position[0] != 0: position[0] -= 1
            else:work=False
        case 's': 
            if position[0] != 5:position[0] += 1
            else: work=False
        case 'd':
            if position[1] != 4:position[1] += 1
            else:work=False
        case 'a': 
            if position[1] != 0: position[1] -= 1
            else:work=False
    os.system('cls')
    game_map()
    c(work)
while True: 
    game()