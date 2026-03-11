import random

def random_number():
    return random.randint(17,29)

def die_roll():
    return random.randint(1,6)

def addition_game():
    guess = random_number()
    repeat = True
    crashed = False
    addition_total = 0
    times_added = 0

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
        print(f"Final total:\t{addition_total}")
        distance_guess = guess - addition_total

        if distance_guess == 0:
            print(f"Congratulations! You won with 0 away from {guess}!\nYou won with {times_added} dice rolled!")
        elif -5 <= distance_guess <= 5:
            print(f"You were {abs(distance_guess)} away from {guess}!\nYou won with {times_added} dice rolled!")
        else:
            print("Invalid try - try again")

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