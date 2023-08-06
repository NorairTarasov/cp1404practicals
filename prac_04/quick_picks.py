import random

NUMBERS_PER_ROW = 6
MAXIMUM = 45
MINIMUM = 1


def main():
    """Quick picks program - choose sets of random numbers."""
    quick_picks_amount = int(input("How many quick picks? "))
    while quick_picks_amount < 0:
        print("Input is Invalid")
        quick_picks_amount = int(input("How many quick picks? "))

    for i in range(quick_picks_amount):
        quick_picks_list = []
        for j in range(NUMBERS_PER_ROW):
            random_number = random.randint(MINIMUM, MAXIMUM)
            while random_number in quick_picks_list:
                random_number = random.randint(MINIMUM, MAXIMUM)
            quick_picks_list.append(random_number)
        quick_picks_list.sort()
        print(" ".join(f"{number:2}" for number in quick_picks_list))


main()