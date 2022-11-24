### Rock Paper Scissors challenge with grapichs and list
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice=input("What do you wannt to chosse? Type 1 for rock, 2 for paper, 3 for scissors\n")
user_choice=int(user_choice)-1



if user_choice > 2 or user_choice < 0:
  print("You typed an invalid number, you lose!")

else:
    game_choice=[rock, paper, scissors]

    print(f"User Choice:\n{game_choice[user_choice]}")
    if user_choice==0:
        print(f"{user_choice}=Rock")
    elif user_choice==1:
        print(f"{user_choice}=Paper")
    else:
        print(f"{user_choice}=Scissor")
    computer_choice=random.randint(1,3)
    computer_choice=int(computer_choice-1)


    print(f"Computer Choice:\n{game_choice[computer_choice]}")
    if computer_choice == 0:
        print(f"{computer_choice}=Rock")
    elif computer_choice == 1:
        print(f"{computer_choice}=Paper")
    else:
        print(f"{computer_choice}=Scissor")
    if user_choice==0 and computer_choice==0:
        print("Match Draw")
    elif user_choice==0 and computer_choice==1:
        print("Computer won")
    elif user_choice==0 and computer_choice==2:
        print("User Won")
    elif user_choice==1 and computer_choice==0:
        print("User won")
    elif user_choice==1 and computer_choice==1:
        print("Match Draw")
    elif user_choice==1 and computer_choice==2:
        print("Computer Won")
    elif user_choice==2 and computer_choice==0:
        print("Computer Won")
    elif user_choice==2 and computer_choice==1:
        print("User won")
    elif user_choice==2 and computer_choice==2:
        print("Match Draw")



