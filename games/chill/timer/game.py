import time
AUTHOR = "Yugo206"

def run():
    print(f"Game by {AUTHOR}")
    print("=== Timer ===")

    try:
        seconds = int(input("Enter seconds: "))
    except:
        print("Invalid input")
        return

    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)

    print("Time's up!")