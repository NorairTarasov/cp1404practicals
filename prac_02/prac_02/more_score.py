import random


def main():
    number_of_scores = int(input("Enter number of scores: "))
    file_input(number_of_scores)


def file_input(number_of_scores):
    file = open('results.txt', 'w')
    for i in range(0, number_of_scores):
        score = random.randint(0, 100)
        if score < 50:
            sentence = f"{score} is Bad"
        elif score > 90:
            sentence = f"{score} is Excellent"
        else:
            sentence = f"{score} is Passable"
        file.write(f"{sentence}\n")
    file.close()

main()

