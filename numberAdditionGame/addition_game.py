import random
import os

def random_number():
    return random.randint(0,29)

def die_roll():
    return random.randint(1,6)

def points_system(usage, current_game):
    with open("lifetime_scores.txt", "r") as file:
        total_wins = int(file.readline().strip().split(" = ")[1])
        total_points = int(file.readline().strip().split(" = ")[1])

    with open("lifetime_scores.txt", "w") as file:
        if current_game:
            total_wins += 1
            total_points += usage
        else:
            if total_points - usage < 0:
                total_points = 0
            else:
                total_points -= usage

        file.write(f"Total wins = {total_wins}\n")
        file.write(f"Total points = {total_points}\n")

        print(f"Total wins = \t{total_wins}")
        print(f"Total points = \t{total_points}")


def addition_game():
    game_won = crashed = False
    guess = random_number()
    repeat = True
    addition_total = times_added = 0
    score_tracker = "lifetime_scores.txt"

    if os.path.exists(score_tracker):
        with open(score_tracker, "r") as file:
            print(file.read())
    else:
        with open(score_tracker, "w") as file:
            file.writelines("Lifetime Score = 0\n")
            file.writelines("Points = 100")
            print(file.read())

    while repeat:
        print(f"Value to reach:\t{guess}")
        print(f"Current total:\t{addition_total}")

        new_num = input("Do you want to roll the die?\t")
        try:
            if new_num.lower() in ["", "yes", "y", "yeah", "yep", "yup", "ye", "yh"]:
                addition_total += die_roll()
                times_added += 1
            else:
                repeat = False
                print("Game Over")
        except ValueError:
            repeat = False
            crashed = True
            print("Invalid input - game crashed")

    if not crashed:
        used_points = times_added * 5
        print(f"Final total:\t{addition_total}")

        if addition_total == guess:
            print(f"Congratulations! You got {guess}!\nYou won with {times_added} dice rolled!")
            used_points = 50
            game_won = True
        else:
            print(f"You were unable to get {guess}")

        points_system(used_points, game_won)

while True:
    addition_game()

    try:
        again = int(input("Do you want to play again? [1] yes [2] no\t"))
        if again == 1:
            print("Game Restarting...")
            continue
        else:
            print("Game ended")
            break
    except ValueError:
        print("Invalid input - game crashed")
        break