import random

secret_number = random.randint(1, 10)

attempts = 1

guess = int(input("Guess a number between 1 and 10: "))

while guess != secret_number:
    if guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    attempts += 1

    guess = int(input("Try again: "))

print("Congratulations! You guessed the secret number: ", secret_number)
print("You guessed the secret number in", attempts, "attempts")