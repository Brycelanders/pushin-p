import random
from flip import coin_flip

def get_flip():
    answer = random.choice(coin_flip)
    return answer.upper()

def start(answer):
    tries = 1
    guessed = False
    guessed_flips = []
    print("Welcome to the game")
    print("\n")

    while not guessed and tries > 0:
        guess = input("heads or tails: ")
        guessed_flips.append(guess)

        if guess.upper() == answer:
            guessed == True
            print("You Won")
        else:
            tries -= 1
            if tries == 0:
                print("Game over")
            



def main():
   answer = get_flip()
   
   start(answer)
   while input("play again? (Y/N)").upper() == "Y":
        answer = get_flip()
        start(answer)
main()