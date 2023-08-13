

def main():
    name_of_email = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        yes_or_no = input(f"Is your name {name}? (Y/n) ").upper()
        if (yes_or_no != "Y") and (yes_or_no != ""):
            name = input("Name: ")
        name_of_email[email] = name
        email = input("Email: ")
    for email, name in name_of_email.items():
        print(f"{name} ({email})")


def get_name(email):
    at = email.split("@")[0]
    name_pieces = at.split(".")
    name = " ".join(name_pieces).title()
    return name


main()
