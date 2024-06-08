# # write 'hello world' to the console
# print('hello world')

import random
def get_computer_choice():
    return random.choice(["rock","paper","scissors"])
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif(player_choice=="rock" and computer_choice=="scissors")or\
        (player_choice=="paper" and computer_choice=="rock")or\
        (player_choice=="scissors" and computer_choice=="paper"):
        return "win"
    else:
        return "lose"
def print_result(result, player_choice, computer_choice):
    if result =="win":
         print(f"You chose {player_choice} and the computer chose {computer_choice}. You win!")
    elif result == "lose":
        print(f"You chose {player_choice} and the computer chose {computer_choice}. You lose!")
    else:
        print(f"You chose {player_choice} and the computer chose {computer_choice}. It's a tie!")
def play_game():
    score={"wins":0,"losses":0,"ties":0}
    while True:
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        print_result(result, player_choice, computer_choice)

        if result == "win":
            score["wins"] += 1
        elif result == "lose":
            score["losses"] += 1
        else:
            score["ties"] += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print(f"Final score: {score['wins']} wins, {score['losses']} losses, {score['ties']} ties")

if __name__ == "__main__":
    play_game()
