is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:  # it is ValueError because [ValueError: invalid literal for int() with base 10: 'ef']
        print("Please enter a valid integer.")
print(f"Valid result is:", result)
