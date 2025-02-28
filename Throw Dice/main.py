import random

def throw_dice(n):
    for i in range(n):
        random_num = random.randint(1, 6)
        print(f"Throw from dice {i+1}: {random_num}")


def run():
    number = int(input("Welcome to Throw a Dice! \nHow many dice would you like to throw?:"))
    throw_dice(number)

if __name__ == "__main__":
    run()
