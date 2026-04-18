AUTHOR = "bhavyainturi9"
import random

def run():
    print(f"Welcome to Coin Flip by {AUTHOR}")

    user_choice = input("Guess heads or tails: ").lower()

    if user_choice not in ["heads", "tails"]:
        print("Invalid choice! Please choose heads or tails.")
        return

    result = random.choice(["heads", "tails"])
    print(f"Coin landed on: {result}")

    if user_choice == result:
        print("🎉 You win!")
    else:
        print("😢 You lose!")
