import random

WORDS = ["python", "hangman", "banana", "laptop", "school", "wizard", "guitar", "rocket"]

def hangman():
    secret = random.choice(WORDS).lower()
    guessed = set()
    wrong = 0
    max_wrong = 6

    while True:
        # Build display word
        display = " ".join([ch if ch in guessed else "_" for ch in secret])
        print("\nWord:", display)
        print(f"Wrong guesses: {wrong}/{max_wrong}")
        print("Guessed:", " ".join(sorted(guessed)) if guessed else "(none)")

        # Win check
        if all(ch in guessed for ch in secret):
            print("\nYou win! The word was:", secret)
            break

        # Lose check
        if wrong >= max_wrong:
            print("\nYou lose! The word was:", secret)
            break

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter ONE letter (a-z).")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.add(guess)

        if guess in secret:
            print("Nice! That letter is in the word.")
        else:
            wrong += 1
            print("Nope! That letter is not in the word.")

if __name__ == "__main__":
    hangman()
