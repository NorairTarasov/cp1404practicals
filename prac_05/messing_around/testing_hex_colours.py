FILENAME = "hex_colours.txt"

file = open(FILENAME, "r")

hex_colours_list = []
hex_names_list = []

for i in file:
    index = i.find("#")
    hex_colours_list.append(i[index+1:].upper())
    hex_names_list.append(i[0:index])

print(hex_colours_list)
print(hex_names_list)

color_code = input("Enter color code: #").upper()

while color_code != "":

    for j in file:
        name = j.find("#")
        if color_code == hex_colours_list[name+1:]:
            print(f"#{color_code}", "is", hex_names_list[0:name])

    if color_code not in hex_colours_list:
        print("Invalid short state")
    color_code = input("Enter color code: #").upper()

file.close()
