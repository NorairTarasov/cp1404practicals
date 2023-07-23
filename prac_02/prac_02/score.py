"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
if (score < 0) or (score > 100):
    print(f"{score} is Invalid score")
elif score < 50:
    print(f"{score} is Bad")
elif score > 90:
    print(f"{score} is Excellent")
else:
    print(f"{score} is Passable")
