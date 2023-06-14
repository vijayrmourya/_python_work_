def width_height_area(height, base):
    """
    calculates the area of the triangle given a given height and base length
    :param height(float): height of the triangle
    :param base(float): base length of the triangle
    :return(float): area of the triangle
    """
    return ((base*height)/2)


def sides_area(side_1, side_2, side_3):
    """
    calculates the area of triangle given length of its sides
    :param side_1(float): length of the side-1
    :param side_2(float): length of the side-2
    :param side_3(float): length of the side-3
    :return(float): area of triangle
    """
    semi_param = (side_1+side_2+side_3)
    return ((semi_param*(semi_param-side_1)*(semi_param-side_2)*(semi_param-side_3))**0.5)


if __name__ == '__main__':
    try:
        print("Welcome to Area of Triangle calculator!\n")
        method = input(
            'enter "method-1" for calculating area with "base" and "height" and enter "method-2" for calculating area with "sides"')
        match method:
            case 'method-1':
                height = float(
                    input('enter "height" for calculating area with:'))
                base = float(input('enter "base" for calculating area with:'))
                print(
                    f"Area of triangle with height = {height} and length = {base} is: {width_height_area(height, base)} units.\n")
            case 'method-2':
                side_1 = float(
                    input('enter "side-1" for calculating area with:'))
                side_2 = float(
                    input('enter "side-2" for calculating area with:'))
                side_3 = float(
                    input('enter "side-3" for calculating area with:'))
                print(
                    f"Area of triangle with sides - {side_1} {side_2} {side_3} is: {sides_area(side_1, side_2, side_3)} units.\n")
            case _:
                print("please choose valid method")

    except Exception as E:
        print("Some Error Occured!", E)
