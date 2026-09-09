score = 0

print("Welcome to the Quiz Game!")
print("-------------------------")

# Question 1
print("\n1. What is the capital of France?")
print("A. London")
print("B. Paris")
print("C. Rome")
print("D. Madrid")

answer = input("Your answer: ").upper()

if answer == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is Paris.")

# Question 2
print("\n2. How many legs does a spider have?")
print("A. 6")
print("B. 8")
print("C. 10")
print("D. 12")

answer = input("Your answer: ").upper()

if answer == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is 8.")

# Question 3
print("\n3. Which language are you using for this game?")
print("A. Python")
print("B. Java")
print("C. C++")
print("D. HTML")

answer = input("Your answer: ").upper()

if answer == "A":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is Python.")

# Final score
print("\n-------------------------")
print("Quiz complete!")
print("Your score:", score, "/ 3")

if score == 3:
    print("Excellent! 🎉")
elif score == 2:
    print("Good job!")
else:
    print("Keep practicing!")
