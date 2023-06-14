# Program to check if a number is prime or not

def check_prime(num):
    """
    Check if a number is prime
    :param num: Number to check
    :return: True if the number is prime, False otherwise
    """
    if num > 2:
        # check for factors
        for i in range(2, int(number**0.5) + 1):
            if (num % i) == 0:
                return False
        else:
            return True


if __name__ == '__main__':
    try:
        number = int(
            input('enter the number you want to check if it\'s prime of not: '))
        if check_prime(number):
            print(f'{number} is a prime!')
        else:
            print(f'{number} is not a prime')
    except TypeError as TE:
        print("some error occured please enter valid year!", TE)
    except Exception as e:
        print("some error occured!", e)
