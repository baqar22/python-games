
import random

# Choose a random number between 1 and 1000
secret_number = random.randint(1, 1000)

# Give the player 10 attempts
attempts = 10

print("I'm thinking of a whole number between 1 and 1000.")
print("You have 10 attempts to guess it!")

for attempt in range(1, attempts + 1):
    try:
        guess = int(input(f"Attempt {attempt}/10 - Enter your guess: "))

        if guess < 1 or guess > 1000:
            print("Please enter a whole number between 1 and 1000.")
            continue

        if guess < secret_number:
            print("Too small! Try a larger number.")

        elif guess > secret_number:
            print("Too large! Try a smaller number.")

        else:
            print(f"Correct! You guessed the number in {attempt} attempts!")
            break

    except ValueError:
        print("Please enter a whole number.")

else:
    print(f"Out of attempts! The number was {secret_number}.")
