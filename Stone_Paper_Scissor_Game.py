print("WELCOME TO THE STONE-PAPER-SCISSOR GAME\n")
print("Please Note:-\n"
      "1). Stone stands by s\n"
      "2). Paper stands by p\n"
      "3). Scissor stands by c\n")

import random
lst=["s","p","c"]
human_points=0
computer_points=0
no_of_chances=0
total_chances=9


while no_of_chances<total_chances: #here i hve put the condn that if no of chances < total chaces, it will take i/p otherwise not
      _input=input("Please enter your i/p from s-p-c\n") #its human input
      _computer=random.choice(lst)#its computer random input,

      if _input==_computer:
            print("It's a TIE")
            print(f"human i/p is {_input} and compuer i/p is {_computer}\n")
      elif _input=="s" and _computer=="p":
            print("Computer wins")
            no_of_chances += 1
            computer_points += 1
            print(f"human i/p is {_input} and compuer i/p is {_computer}")
            print(f"human points is {human_points} and computer points is {computer_points}\n")
      elif _input == "s" and _computer == "c":
            print("Human wins")
            no_of_chances += 1
            human_points += 1
            print(f"human i/p is {_input} and compuer i/p is {_computer}")
            print(f"human points is {human_points} and computer points is {computer_points}\n")
      elif _input == "p" and _computer == "s":
            print("Human wins")
            no_of_chances += 1
            human_points += 1
            print(f"human i/p is {_input} and compuer i/p is {_computer}")
            print(f"human points is {human_points} and computer points is {computer_points}\n")
      elif _input == "p" and _computer == "c":
            print("Computer wins")
            no_of_chances += 1
            computer_points += 1
            print(f"human i/p is {_input} and compuer i/p is {_computer}")
            print(f"human points is {human_points} and computer points is {computer_points}\n")
      elif _input == "c" and _computer == "s":
            print("Computer wins")
            no_of_chances += 1
            computer_points += 1
            print(f"human i/p is {_input} and compuer i/p is {_computer}")
            print(f"human points is {human_points} and computer points is {computer_points}\n")
      elif _input == "c" and _computer == "p":
            print("Human wins")
            no_of_chances += 1
            human_points += 1
            print(f"human i/p is {_input} and compuer i/p is {_computer}")
            print(f"human points is {human_points} and computer points is {computer_points}\n")
      else:
            print("Invalid Input, please enter correct")

      print(f"no of chances left is {total_chances-no_of_chances} out of {total_chances}\n")

if human_points>computer_points:
      print("AND THE WINNER IS HUMAN\n")
elif computer_points>human_points:
      print("AND THE WINNER IS COMPUTER\n")
else:
      print("ITS A TIE")
print(f"total human points is {human_points} and computer points is {computer_points}\n")

print("Thank you for playing the game, YOU ARE THE HERO")


