FILENAME = "name.txt"
ANOTHER_FILENAME = "numbers.txt"

# Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
in_file = open(FILENAME, 'w')
username = input("Enter your name: ").title()
in_file.write(username)
in_file.close()

# Write code that opens "name.txt" and reads the name (as above) then prints,
in_file = open(FILENAME, 'r')
print(f"Your name is {in_file.read()}")
in_file.close()

# Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result
another_file = open(ANOTHER_FILENAME, 'r')
first = int(another_file.readline())
second = int(another_file.readline())
total_task_one = first + second
another_file.close()
print(total_task_one)

another_file = open(ANOTHER_FILENAME, 'r')
total_task_two = 0
for line in range(1, 3):
    number = int(another_file.readline())
    total_task_two += number
another_file.close()
print(total_task_two)
