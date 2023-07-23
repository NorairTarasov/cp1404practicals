"""
(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit
"""
import score
choices = ("(G)et score"
           "\n(P)rint result"
           "\n(S)how stars"
           "\n(Q)uit")
print(choices)
choice = input(">>> ").title()
while choice != "Q":
    if choice == "G":
    elif choice == "P":
    elif choice == "S":
    print(choices)
    choice = input(">>> ").title()