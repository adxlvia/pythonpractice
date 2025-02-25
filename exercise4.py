import random
import time

def generate_wheel():
    spaces = []
    for i in range(18):
        spaces.append("red")
        spaces.append("black")
    for i in range(2):
        spaces.append("green")
    return spaces

def spin_wheel(spaces):
    return random.choice(spaces)

def play_game():
    spaces = generate_wheel()

    money = 1000
    print("you have $" + str(money))

    bet = input("how much do you want to bet?")
    bet = int(bet)
    color = input("what color do you want to be on?")

    print("the wheel is spinning.....")
    time.sleep(2)

    landed = spin_wheel(spaces)
    print(landed)

play_game()


