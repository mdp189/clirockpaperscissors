import random
import time

choices = {
    "no choice": 0,
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}
nums_to_choices = {
    0: "no choice",
    1: "rock",
    2: "paper",
    3: "scissors",
}


class GameIsOver(Exception):  # Idea adapted from user Aaron Hall from
    # https://stackoverflow.com/questions/189645/how-to-break-out-of-multiple-loops
    pass


def reset_values():
    global cpu_score, game_round, player_score, player_choice, cpu_choice
    cpu_choice = 0
    player_choice = 0
    player_score = 0
    cpu_score = 0
    game_round = 1


def player_loss():
    global cpu_score
    print(f'You lost that round!')
    cpu_score = + 1


def player_win():
    global player_score
    print(f'You won that round!')
    player_score = + 1


def tie():
    print("Tie! No points awarded.")


def choose_winner():
    if player_choice == cpu_choice:
        tie()
    elif player_choice == 1 and cpu_choice == 2:
        player_loss()
    elif player_choice == 2 and cpu_choice == 3:
        player_loss()
    elif player_choice == 1 and cpu_choice == 3:
        player_win()
    elif player_choice == 2 and cpu_choice == 1:
        player_win()
    elif player_choice == 3 and cpu_choice == 1:
        player_loss()
    elif player_choice == 3 and cpu_choice == 2:
        player_win()


def game_over():
    print(f" ")
    if player_score > cpu_score:
        print("You won the game!")
    if player_score < cpu_score:
        print("You lost the game!")
    if player_score == cpu_score:
        print("The game is a tie!")
    time.sleep(1)


def ask_play_again():
    while True:
        play_again = input("Would you like to play again? (y/n) ").strip().lower()
        if play_again == "n":
            raise GameIsOver
        elif play_again == "y":
            break
        else:
            print("Input not recognized. Must be either y or n.")


def cpu_play():
    global cpu_choice
    cpu_choice = random.randint(1, 3)
    time.sleep(1)
    print(f"The computer chose {nums_to_choices[cpu_choice]}")


first_time = True
try:
    while True:
        if not first_time:
            ask_play_again()
        reset_values()
        while True:
            try:
                amt_of_rounds = int(input("How many round would you like to play to the best of? (ex. Best of 5) "))
                break
            except:
                print("Input not recognized. Please input an integer.")
        while True:
            print(f" " * 100)
            print(f"Round #{game_round}")
            while True:
                try:
                    player_choice = choices[str(input("Rock, Paper, or Scissors? ")).lower().strip()]
                    break
                except:
                    print("Input not recognized. Choose either Rock, paper, or scissors.")
            cpu_play()
            choose_winner()
            print(f"Player's score is {player_score}")
            print(f"Computer's score is {cpu_score}")
            game_round = game_round + 1
            if game_round > amt_of_rounds or player_score * 2 > amt_of_rounds or cpu_score * 2 > amt_of_rounds:
                game_over()
                first_time = False
                break
            time.sleep(1)
except GameIsOver:
    pass
except:
    print("An unknown error occurred.")
