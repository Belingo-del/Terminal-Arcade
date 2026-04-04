import os
import importlib.util

GAMES_PATH = "games"


def load_games():
    games = {}
    errors = []

    for category in os.listdir(GAMES_PATH):
        category_path = os.path.join(GAMES_PATH, category)

        if not os.path.isdir(category_path):
            continue

        games[category] = []

        for game_name in os.listdir(category_path):
            game_path = os.path.join(category_path, game_name, "game.py")

            if not os.path.isfile(game_path):
                continue

            try:
                spec = importlib.util.spec_from_file_location(game_name, game_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                if hasattr(module, "run"):
                    games[category].append((game_name, module.run))
                else:
                    errors.append(f"{game_name} has no run()")

            except Exception as e:
                errors.append(f"{game_name} failed: {e}")

    return games, errors


def menu(games):
    while True:
        print("\n=== Categories ===")
        categories = list(games.keys())

        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")

        print("0. Exit")

        choice = input("> ")

        if choice == "0":
            break

        try:
            category = categories[int(choice) - 1]
            game_menu(category, games[category])
        except:
            print("Invalid choice")


def game_menu(category, games_list):
    while True:
        print(f"\n=== {category} ===")

        for i, (name, _) in enumerate(games_list, 1):
            print(f"{i}. {name}")

        print("0. Back")

        choice = input("> ")

        if choice == "0":
            break

        try:
            _, run_func = games_list[int(choice) - 1]
            run_func()
        except:
            print("Error launching game")


def main():
    games, errors = load_games()

    if errors:
        print("Some games failed to load:")
        for err in errors:
            print("-", err)
    else:
        print("All games loaded successfully.")

    menu(games)


if __name__ == "__main__":
    main()