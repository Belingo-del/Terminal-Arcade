AUTHOR = "Yugo206"

def run():
    print(f"Game by {AUTHOR}")
    questions = [
        ("What is 2 + 2?", "4"),
        ("What is the capital of France?", "paris"),
        ("What color is the sky?", "blue"),
    ]

    score = 0

    print("=== Quiz ===")

    for q, a in questions:
        answer = input(q + " ").lower()

        if answer == a:
            print("Correct!")
            score += 1
        else:
            print("Wrong! Answer was:", a)

    print(f"\nFinal score: {score}/{len(questions)}")