import random
print("LET'S PLAY RANDOM GUESSING !!")
top_range = int(input("Enter a number for higher limit(positive number): "))

if top_range<0:
    print("Please enter a number greater than zero ")
    quit()

rand_num = random.randint(0, top_range)
guess = 0

while True:
    guess += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time")
        continue

    if user_guess == rand_num:
        print("Yes, you got it !!")
        break
    elif user_guess > rand_num:
        print("You were above the number")
    else:
        print("You were below the number")

print("You got it in",guess,"guesses")

