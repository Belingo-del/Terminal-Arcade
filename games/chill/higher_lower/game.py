import random

AUTHOR = "Deepak Singh"

def run():
    print(f"Game by {AUTHOR}")
    print("=== Higher or Lower ===")
    
    current_number = random.randint(1, 100)
    score = 0
    
    while True:
        print(f"\nCurrent number: {current_number}")
        guess = input("Next number will be Higher (h) or Lower (l)? (q to quit): ").lower()
        
        if guess == 'q':
            print(f"\nYou quit! Final Score: {score}")
            break
        
        if guess not in ['h', 'l']:
            print("Invalid input! Use 'h', 'l', or 'q'.")
            continue
            
        next_number = random.randint(1, 100)
        while next_number == current_number:
            next_number = random.randint(1, 100)
            
        print(f"Next number was: {next_number}")
        
        if (guess == 'h' and next_number > current_number) or \
           (guess == 'l' and next_number < current_number):
            score += 1
            print(f"Correct! Score: {score}")
            current_number = next_number
        else:
            print(f"Wrong! Game Over. Final Score: {score}")
            break
            
    print("\nThanks for playing!")
