import re

"""
credit_card_validator: to validate a credit card number
"""


def details():
    """
    to print rules of a valid credit card number
    :return: 0
    """
    print(
        f"It must contain exactly 16 digits.\nIt should only contain 0-9 digits.\nIt must start with either 9 or 7 or "
        f"3.\nIt may have digits in a group of 4 with a separator (-).\nIt must not contain any other symbols such as _ "
        f"or space(‘ ‘).\n{'-' * 50}"
    )
    return 0


def validate_card(card_number):
    """
    function to validate the card number using regular expression
    :param card_number: type= str | card number to be validated
    :return: bool based on results
    """
    pattern = '^[973][0-9]{15}|[973][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$'
    result = re.match(pattern, card_number)
    return True if result else False


if __name__ == "__main__":
    details()
    while 1:
        card_number = input("Please enter the card number: ")
        print(card_number + "->" + "valid card") if validate_card(card_number) else print(
            card_number + "->" + "Invalid card")
        another = input("Do you want to check another card (y/n):")
        if another == 'n':
            break
