import random

user_score = 0
computer_score = 0

option = ["rock","paper","scissor"]

while True:
    user_input = input("Choose your choice (rock/paper/scissor) or Q to quit: ").lower()
    if user_input == "q":
        break
    
    elif user_input not in option:
        print("Kindly enter a valid input")
        continue

    rand_num = random.randint(0,2)
    comp_input = option[rand_num]
    print("Computer picked :",comp_input)

    if user_input == "rock" and comp_input == "scissor":
        print("You win !")
        user_score+=1
    elif user_input == "scissor" and comp_input == "paper":
        print("You win !")
        user_score+=1
    elif user_input == "paper" and comp_input == "rock":
        print("You win !")
        user_score+=1
    elif user_input == "rock" and comp_input == "rock":
        continue
    elif user_input == "paper" and comp_input == "paper":
        continue
    elif user_input == "scissor" and comp_input == "scissor":
        continue
    else:
        print("Computer wins !!")
        computer_score += 1

print("Your score :",user_score)
print("Computer score :",computer_score)

if user_score>computer_score:
    print("You got higher score than computer..")
    print("You win !!")
elif user_score<computer_score:
    print("Computer got higher score than you..")
    print("You lost !!")
else:
    print("Goodbye !!")
    
    
