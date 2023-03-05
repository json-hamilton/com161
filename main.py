from sys import exit

global smallest_number
global largest_number
global total


def validate(user_input):
    if len(user_input) > 8:
        print("The binary number can only be 8 digits in length \n")
        return False
    try:
        return int(user_input, 2)
    except ValueError:
        print("Your input can only use the digits 0 or 1 \n")
        return False


def to_binary(number):
    if number < 0:
        return "-" + bin(number)[3:]
    return bin(number)[2:]


def while_loop():
    count = 0
    smallest_number = None
    largest_number = None
    while True:
        user_input = input("Enter a binary number, or q to view the results >>> ")
        if user_input == "q":
            break
        user_input = validate(user_input)
        if user_input is False:
            continue
        count += 1
        if smallest_number is None or smallest_number > user_input:
            smallest_number = user_input
        if largest_number is None or largest_number < user_input:
            largest_number = user_input
    print("\033[1m" + "\033[4m" + "Results".center(120, ' ') + "\033[0m\n")
    if count == 0:
        print("There were no binary numbers input.")
    else:
        print(f"There were {count} binary numbers input.")
        print(
            f"The difference between the smallest number {to_binary(smallest_number)} ({smallest_number}) and the "
            f"largest number {to_binary(largest_number)} ({largest_number}) is"
            f" {to_binary(largest_number - smallest_number)} ({largest_number - smallest_number})")
        print("_" * 120)


def for_loop():
    global smallest_number
    global largest_number
    global total
    smallest_number = None
    largest_number = None
    total = 0
    try:
        count = int(input("How many binary numbers would you like to enter? >>> "))
        if count < 0:
            print("Do not enter a negative number")
            for_loop()
    except ValueError:
        print("Please enter a number")
        for_loop()
    total = do_for_loop(count)
    print("\033[1m" + "\033[4m" + "Results".center(120, ' ') + "\033[0m\n")
    if smallest_number is None:
        print("There were no binary numbers input.")
    else:
        print(f"The total of the binary numbers input is {to_binary(total)} ({total})")
        print(
            f"The smallest number was {to_binary(smallest_number)} ({smallest_number}) and the largest number was {to_binary(largest_number)} ({largest_number})")
        print("_" * 120)


def do_for_loop(count):
    global smallest_number
    global largest_number
    global total
    skipped = 0
    for i in range(count):
        user_input = input("Enter a binary number >>> ")
        user_input = validate(user_input)
        if user_input is False:
            skipped += 1
            continue
        if smallest_number is None or smallest_number > user_input:
            smallest_number = user_input
        if largest_number is None or largest_number < user_input:
            largest_number = user_input
        total += user_input
    if skipped != 0:
        do_for_loop(skipped)
    return total


def main():
    print("\033[1m" + "\033[4m" + "Binary Inputter".center(120, ' ') + "\033[0m")
    while True:
        print("\nPlease choose an option by typing in its name:")
        print(u"\u2022" + " \033[1m f:" + "\033[0m Use a for loop to input binary numbers")
        print(u"\u2022" + " \033[1m w:" + "\033[0m Use a while loop to input binary numbers")
        print(u"\u2022" + " \033[1m q:" + "\033[0m Exit the application")

        option_not_chosen = True
        while option_not_chosen:
            user_input = input("\nPlease choose an option >>> ")
            if user_input == "f":
                print(
                    "This function will read in binary numbers that you input, and tell you the total, "
                    "the smallest number and the largest number.")
                for_loop()
                option_not_chosen = False
            elif user_input == "w":
                print(
                    "This function will read in binary numbers that you input, and tell you how many there are and "
                    "the difference between the smallest and largest.")
                while_loop()
                option_not_chosen = False
            elif user_input == "q":
                exit("User quit the program")
            else:
                print("Input not recognised. Try again.")


main()
