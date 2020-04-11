def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number < 0:
        return None

    if (number == 0) or (number == 1):
        return number

    sqrt = number / 2;
    temp = 0;

    while(sqrt != temp):
        temp = sqrt;
        sqrt = ( number/temp + temp) / 2;

    return round(sqrt);

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")