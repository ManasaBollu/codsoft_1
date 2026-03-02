import random
def get_user_choice():
    while True:
        user_choice = input("Enter your choice(rock,paper,scissor)")
        if user_choice.lower() in ["rock","paper","scissor"]:
            return user_choice.lower()
        print("Invalid input")
def get_computer_choice():
    return random.choice(["rock","paper","scissor"])
def determain_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "It's a tie"
    elif ((user_choice == "rock" and computer_choice == "scissor") or (user_choice == "scissor" and computer_choice == "paper") 
          or (user_choice == "paper" and computer_choice == "rock")):
        return "you win"
    else:
        return "you lose"
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"you choice : {user_choice}")
    print(f"computer choice : {computer_choice}")
    print(determain_winner(user_choice,computer_choice))
def main():
    while True:
        play_game()
        play_again = input("do you want to play again? (yes/no) : ")
        if play_again.lower() != "yes":
            break
if __name__ == "__main__":
    main()
