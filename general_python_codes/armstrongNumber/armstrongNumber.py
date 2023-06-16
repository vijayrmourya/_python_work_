"""
What is Armstrong Number?
An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself.

For example, 153 is an armstrong number

153 = 1^3 + 5^3 + 3^3
153 = 1 + 125 + 27
153 = 153
Note: Each number is raised to the power of 3, because, the number of digits in 153 is 3.
"""


def armstrong_check_arithematic_method(number):
    """
    takes a number and tells if its armstrong number or not
    :param number: number to check
    :return: True if the number is armstrong, False otherwise
    """
    power = 0
    numbers = []
    save = number
    while number > 0:
        power = power + 1
        numbers.append(number % 10)
        number = number // 10
    return True if int(sum([num**power for num in numbers])) == int(save) else False


def armstrong_check_string_method(number):
    """
    takes a number and tells if its armstrong number or not
    :param number: number to check
    :return: True if the number is armstrong, False otherwise
    """
    num = list(str(number))
    powered_sum = sum([int(i)**len(num) for i in num])
    return True if powered_sum == int(number) else False
    # return True if sum([int(i)**len(list(str(number))) for i in list(str(number))]) == int(number) else False


if __name__ == '__main__':
    number = int(
        input('Please enter number to check if its armstrong or not: '))
    if armstrong_check_string_method(number):
        print(f'{number} is armstrong!')
    else:
        print(f'{number} is not armstrong')
    if armstrong_check_arithematic_method(number):
        print(f'{number} is armstrong!')
    else:
        print(f'{number} is not armstrong')
