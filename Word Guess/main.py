import random

words = ["blueberry", "grape", "apple", "mango", "watermelon"]

word = random.choice(words)

print("Guess the characters")

guesses = ''

turns = 12

while turns > 0:
    failed = 0

    for char in guesses:
        print(char)

    else:
        print("_")

        failed += 1

    if failed == 0:
        print("You win!")

        print("This word is ", word)
        break

    guess = input("guess a character: ")

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")

        print("You have", + turns, "more guesses")

        if turns == 0:
            print("You Loose")
