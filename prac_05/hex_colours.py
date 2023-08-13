COLOURS = {"Fuzzy Wuzzy": "#87421f", "GO Green": "#00ab66", "Chocolate": "#d2691e",
           "Bright Maroon": "#c32148", "Zaffre": "#0014a8", "Ultramarine Blue": "#4166f5",
           "Upsdell Red": "#ae2029", "Van Dyke Brown": "#664228",
           "Oxford Blue": "#002147", "Pacific Blue": "#1ca9c9",
           "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
           "Rust": "#b7410e", "SaddleBrown": "#8b4513",
           "Beige": "#f5f5dc", "Bisque1": "#ffe4c4"}

name = input("Enter a colour name (write nothing to skip to hex-code): ")
while name != "":
    print(f"The code for \"{name}\" is {COLOURS.get(name)}")
    name = input("Enter a colour name: ")

