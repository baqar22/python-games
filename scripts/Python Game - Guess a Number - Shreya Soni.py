#name = input("What is your name? ")
#age = int(input("How old are you? "))

#print(f"hello, {name}!")
#print(f"next year you will be {age + 1 }.")


#first = int(input("Enter first number:"))
#second = int(input("Enter second number:"))
#print(first + second)

#first = float(input("Enter first number:"))
#second = float(input("Enter second number:"))
#print(first + second)

#name = ("Alice")
#age = 15
#print(f"Hello {name}, you are the age of {age}.")
# the most important poitn is to not decorate every message, it is to make the result easy to understand and esay to check.
#name = input("What is your name? ") 
#age = int(input("what is your age? "))
#print(f"hello {name}, I hope you are doing great. This year, you are {age} yeras old")



import random

print("Welcome to Guess the Number!")
print("I have chosen a number between 1 and 500.")
print("You have 5 tries to guess it.")

number = random.randint(1, 400)

for attempt in range(1, 6):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Correct! You guessed the number!")
        break
    elif guess < number:
        print("The number is higher. Try again!")
    else:
        print("The number is lower. Try again!")

    print("You have", 5 - attempt, "tries left.")

if guess != number:
    print("Sorry! You ran out of tries.")
    print("The number was", number)