def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # We check if the input number is negative
    if number < 0:
        return None


    # We check if the input number 0 or 1.
    if (number == 0) or (number == 1):
        return number

    # Declare main variables for the algorithm
    sqrt = number / 2;
    temp = 0;

    # While sqrt not equals temp keep searching
    while(sqrt != temp):
        temp = sqrt;
        sqrt = ( number/temp + temp) / 2;

    return round(sqrt);

# Default Udacity test cases:
print("\nNormal cases:")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# Edge cases added by me:
print("\nEdge cases:")
print ("Pass" if  (5851 == sqrt(34234234)) else "Fail")
print ("Pass" if  (None == sqrt(-1)) else "Fail")
print ("Pass" if  (None == sqrt(-500)) else "Fail")
print ("Pass" if  (100000 == sqrt(10000000000)) else "Fail")