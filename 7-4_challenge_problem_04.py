numbers = [0, 7, 14, 25, 39, 43]

while True:
    answer = input("Guess a number as you like 0 to 50, or Type q to quit:")

    if answer  == "q":
        break

    try:
        answer = int(answer)
        """
        "input" gets object as str-type.
        "int" transforms str-type to int-type.
        """
    except ValueError:
        print("Type number or Type q to quit")
        continue

    if answer in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly!")


