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
        elif four == "0913" or four == "0914" or four == "0920" or four == "0921" or four == "0928" or four == "0929" or four == "0930":
            print("Your Network is Smart")
        elif four == "0909" or four == "0910" or four == "0911" or four == "0912" or four == "0918" or four == "0919":
            print("Your Network is TNT")
        elif four == "0922" or four == "0923" or four == "0932" or four == "0933":
            print("Your Network is Sun")
        elif four == "0915" or four == "0916" or four == "0917" or four == "0925" or four == "0926" or four == "0927":
            print("Your Network is Globe")
        elif four == "0903" or four == "0904" or four == "0905" or four == "0906" or four == "0907":
            print("Your Network is TM")
        elif four == "0901" or four == "0902" or four == "0924":
            print("Your Network is Red")
        elif four == "0991" or four == "0992" or four == "0993" or four == "0994" or four == "0995" or four == "0996" or four == "0997" or four == "0998":
            print("Your Network is DITO")
        else:
            print("Unknown Network")

    except ValueError:
        print("Enter a valid mobile number (11 Digits)!")
