"""
LIST EXERCISES

PART 1
"""

number_list = []
total = 0

for i in range(0, 5):
    number = int(input("Number: "))
    number_list.append(number)

print(f"The first number is {number_list[0]}"
      f"\nThe last number is {number_list[4]}")

number_list.sort()

print(f"The smallest number is {number_list[0]}"
      f"\nThe largest number is {number_list[4]}")

for k in number_list:
    total += k
average = total / 5

print(f"The average of the numbers is {average:.1f}")


"""
PART 2
"""
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username_input = input("Enter your username: ")
if username_input in usernames:
    print("Access granted")
else:
    print("Access denied")
