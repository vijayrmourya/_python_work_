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
    A = int(input("Please enter the number you want prime factorials for:"))
    if A <= 1:
        print("Please select a number greater than 1")
    else:
        choice = 'y'
        print(f"Prime numbers after {A} are:")
        while choice == 'y':
            if is_prime(A):
                print(f"next prime is: {A}")
                A += 1
                choice = input("Do you want to check next prime?(y/n)")
            else:
                A+=1
    break

