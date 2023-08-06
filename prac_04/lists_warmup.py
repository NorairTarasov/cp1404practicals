numbers = [3, 1, 4, 1, 5, 9, 2]
# list always starts from 0 and adds by one

print(numbers[0])
# first number in the list is 3

print(numbers[-1])
# first number from end is 2

print(numbers[3])
# fourth number in the list is 1 (don't forget we still count 0 as first number)

print(numbers[:-1])
# displays every number until first number from end exclusive

print(numbers[3:4])
# displays only numbers from fourth position to fifth without counting ending number

print(5 in numbers)
# there is 5 in the list, so it's True

print(7 in numbers)
# there is no 7 in the list, so it's False

print("3" in numbers)
# there are no string values in the list, so it's False

print(numbers + [6, 5, 3])
# updated list has been displayed with 3 more values added at the end of it
