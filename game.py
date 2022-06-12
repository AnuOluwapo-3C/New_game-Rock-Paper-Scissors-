def Info():
    print("\tHELLO THERE! WELCOME TO ROCK PAPER SCISSORS GAME!")
    print("INSTRUCTIONS:\nBoth the players have three choices namely rock, paper and scissors.")
    print("\nGAME RULES:")
    print("\tSCISSORS beats PAPER")
    print("\tPAPER beats ROCK")
    print("\tROCK beats SCISSORS")
    print("--------------------------------------------------------------------------")
    print("Choose between the two options: ")
    print("\t 1. Play with the computer")
    print("\t 2. Play with a friend")
    print("\t 3. Exit Game")
import random
def play():
    user=input("what  is your choice 'r' for rock, 'p' for paper, 's' for scissors\n")
    user=user.lower()
    computer=random.choice['r','p','s']

    if user == computer:
      return "You and the computer have both chosen{}. It is a tie".format(computer)
    if winner(user, computer):
            return "You have chosen{} a the computer has chosen{}.You won!".format(user, computer)
    return "You have chosen{} and the computer has chosen{}.You lost:(".format(user, computer)
def winner(Player, Opponent):
                #return true the player beat the opponent
                #winning conditions: r>s, s>p, p>r
                if (Player=='r' and  Opponent=='s') or (Player=='s' and Opponen=='p') or (Player=='p' and Opponent=='r'):
                 return True
                 return False

if __name__ == "__game__":
    print(play())