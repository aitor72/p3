def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    max_value = ints[0];
    min_value = ints[0];
    for num in ints:
    	if (num > max_value):
    		max_value = num
    	if (num < min_value):
    		min_value = num

    return (min_value,max_value)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

# Default Udacity test cases:
print("\nNormal cases:")
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


# Edge cases added by me:
print("\nEdge cases:")
print ("Pass" if ((1, 7) == get_min_max([1,2,3,4,5,6,7])) else "Fail")
print ("Pass" if ((0,0) == get_min_max([0])) else "Fail")
print ("Pass" if ((-1,40) == get_min_max([-1,1,2,3,40])) else "Fail")
print ("Pass" if ((-10,-1) == get_min_max([-10,-5,-1])) else "Fail")