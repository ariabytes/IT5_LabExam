# Network Checker

while True:
    try:
        number = str(input("Enter a valid mobile number (11 Digits): "))
        number = number.replace(" ", "")
        length = len(number)
        four = number[0:4]

        if length != 11:
            print("Enter an 11-digit number!")
            continue
        elif number[0:2] != "09":
            print("Invalid Mobile Number (Start with 09)")
            continue
        elif four == "0913" or four == "0914" or four == "0920":
            print("Your Network is Smart")





    except ValueError:
        print("Enter a valid mobile number (11 Digits)!")
