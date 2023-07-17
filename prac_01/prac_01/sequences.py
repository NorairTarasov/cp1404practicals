print("(i) Even\n(ii) Odd\n(iii) Squares\n(iv) Exit")
choice = str(input(">>> ")).lower()
choices = ('i', 'ii', 'iii', 'iv')
while choice != "iv":
    x = int(input("Minimum number: "))
    y = int(input("Maximum number: "))+1
    if x <= y:
        if choice in choices:
            if choice == "i":
                for i in range(x, y):
                    if (i % 2) == 0:
                        print(i, end=' ')
                print()
            if choice == "ii":
                for i in range(x, y):
                    if (i % 2) != 0:
                        print(i, end=' ')
                print()
            if choice == "iii":
                for i in range(x, y):
                    i *= i
                    if i < y:
                        print(i, end=' ')
                print()
        else:
            print("Invalid Choice")
    else:
        print("Invalid Input")
    print("(i) Even\n(ii) Odd\n(iii) Squares\n(iv) Exit")
    choice = str(input(">>> ")).lower()
print("Thank you.")
