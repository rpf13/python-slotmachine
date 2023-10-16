"""
# Your code goes here.
# Write your code to expect a terminal of 80 characters wide and 24 rows high
"""

MAX_LINES = 3


def deposit():
    """
    Prompt the user to enter a deposit amount. Ensure the amount is a positive
    integer before returning it.
    """
    while True:
        amount = input("How much do you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0!")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    """
    Prompt the user to enter the number of lines to bet on. Ensure the input is
    an integer within the valid range before returning it.
    """
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? "
        )
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines!")
        else:
            print("Please enter a number.")

    return lines


def main():
    """
    Main function to execute the betting game operations.
    """
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)


# Execute the main function when the script is run
if __name__ == "__main__":
    main()
