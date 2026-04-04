import random

WORDS = ["python", "arcade", "game", "code", "terminal"]
AUTHOR = "Yugo206"

def run():
    print(f"Game by {AUTHOR}")
    word = random.choice(WORDS)
    guessed = ["_"] * len(word)
    attempts = 6
    used_letters = []

    print("=== Hangman ===")

    while attempts > 0 and "_" in guessed:
        print("\nWord:", " ".join(guessed))
        print("Used letters:", ", ".join(used_letters))
        print("Attempts left:", attempts)

        letter = input("Guess a letter: ").lower()

        if letter in used_letters:
            print("Already used!")
            continue

        used_letters.append(letter)

        if letter in word:
            for i, l in enumerate(word):
                if l == letter:
                    guessed[i] = letter
        else:
            attempts -= 1
            print("Wrong!")

    if "_" not in guessed:
        print("\nYou win! The word was:", word)
    else:
        print("\nYou lost! The word was:", word)