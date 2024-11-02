import random

score = {
  "player": 0,
  "computer": 0
}
continue_playing = True
option = input("Enter rock, paper, or scissors: ")


while (continue_playing):
  if option.lower() in ["rock", "paper", "scissors"]:
    print("You chose: " + option)
    computer_option = random.choice(["rock", "paper", "scissors"])
    if option.lower() == computer_option:
      print("Computer chose: " + computer_option)
      print("It's a tie!")
    elif option.lower() == "rock" and computer_option == "scissors":
        print("Computer chose: " + computer_option)
        print("You win!")
        score["player"] += 1
    else:
        print("Computer chose: " + computer_option)
        print("You lose!")
        score["computer"] += 1
    print("Do you want to play again?")
    continue_playing = input("Enter y to continue or q to quit: ") == "y"
  else:
    print("Invalid input. Please enter rock, paper, or scissors.")
  if continue_playing:
    option = input("Enter rock, paper, or scissors: ")

print("Final score:")
print("g: " + str(score["player"]))
print("Computer: " + str(score["computer"]))
print("Goodbye!")