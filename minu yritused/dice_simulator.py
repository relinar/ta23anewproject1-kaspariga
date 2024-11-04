import random

while True:
    random_roll = random.randint(1, 6)
    roll_again = input("Do you want to roll the dice? [yes, no]: ").strip().lower()

    if roll_again == "yes":
        print("You rolled:", random_roll)
    elif roll_again == "no":
        print("Okay! Thanks for playing!")
        break  
    else:
        print("Please enter 'yes' or 'no'.")
