a = int(input("Enter a number between 1 and 10 : "))

match a:
    case 2:
        print("you won a charger")

    case 4:
        print("you won $4")

    case 6:
        print("you won a camera")

    case _:
        print("better luck next time")