import random
running = True
answerRange = int(input("one in what number do u want the answer to be in? "))
answer = random.randint(1,answerRange)
rounds = 0
def guess(user_guess):
    global rounds
    rounds += 1
    if user_guess == answer:
        #win
        print(f"you win!\nthe answer was indeed {answer}\nThat took you {rounds} rounds\nThanks for playing")
        running = False
    elif user_guess > answer:
        print("Your guess was above the correct answer.")
    else:
        print("Your guess was below the correct answer.")

print("okay the random number has been selected.")
while running:
    userGuess = input("Guess a number: ")
    userGuess = int(userGuess)
    guess(userGuess)