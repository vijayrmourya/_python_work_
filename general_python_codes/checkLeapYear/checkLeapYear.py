# Python program to check if year is a leap year or not

def leap_year(year):
    """
    Check if year is a leap year
    :param year: year to check
    :return: True if year is a leap year
    """
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# output
# 2000 is a leap year

if __name__ == '__main__':
    try:
        year = int(input('enter the year you want to check: '))
        if leap_year(year):
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    except TypeError as TE:
        print("some error occured please enter valid year!", TE)
    except Exception as e:
        print("some error occured!", e)
