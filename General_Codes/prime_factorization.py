import math


def is_prime(n):
    if n == 2:
        return True
    elif n > 2 and n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True


while 1:
    num = A = int(input("Please enter the number you want prime factorials for:"))
    factor = 2
    if A <= 1:
        print("Please select a number greater than 1")
    else:
        while A > 0:
            if is_prime(factor):
                if A % factor == 0:
                    A = A // factor
                    print(f"prime factor: {factor},")
                elif A == 1:
                    A = 0
                else:
                    factor += 1
            else:
                factor += 1
            if A <= 0:
                print(f"above are the prime factorials of {num}")
    cont = input("Do you want to check another number?(y/n)")
    if cont == 'n':
        print("GoodBye")
        break
    elif cont != 'y':
        print("invalid choice exitng")
        break