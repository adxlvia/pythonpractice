import random

# program that has user guess a random number
random_num = random.randint(0, 100)
guess_count = 0

while True:
    guess = int(input("guess a number \n"))
    guess_count += 1

    if guess > random_num:
        print("guess lower")
    elif guess < random_num:
        print("guess higher")
    else:
        print("congratulations")
        print("it took you " + str(guess_count) + " guesses")
        break


