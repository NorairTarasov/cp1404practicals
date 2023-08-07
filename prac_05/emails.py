

def main():
    email_domain = {}
    email = input("Email: ")
    at = email.split("@")[0]
    name_pieces = at.split(".")
    while email != "":
        name = f" {name_pieces}"
        yes_or_no = input(f"Is your name {name}? (Y/n) ").upper()
        if yes_or_no != "":
            if yes_or_no == "Y":
                email = input("Email: ")
                email_domain[email] = name
            else:
                name = input("Name: ")

        for email, name in email_domain.items():
            print(f"{name} ({email})")


main()
