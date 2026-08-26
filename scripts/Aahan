
import random

# Pick a random maximum number
maximum = random.randint(10, 100000)

# Pick the secret number
answer = random.randint(1, maximum)

print("Welcome to the Number Guessing Game!")
print("The number is between 1 and", maximum)
print("You have 10 tries!")

for tries in range(1, 21):
    guess = int(input("Guess a number: "))

    if guess < answer:
        print("Higher!")
    elif guess > answer:
        print("Lower!")
    else:
        print("You got it!")
        print("The answer was", answer)
        print("You got it in", tries, "tries!")
        break

else:
    print("You ran out of tries!")
    print("The answer was", answer)
