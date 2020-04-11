def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    # If input list is empty
    if(len(input_list) == 0):
        return -1;

    # If input list is only one
    if(len(input_list) == 1):
        if (input_list[0] == number):
            return 0;
        else:
            return -1;


    index = 0
    while input_list[index] < input_list[index + 1]:
        index += 1
        if index + 1 == len(input_list):
            index = len(input_list) // 2
            break
    index += 1

    if number in input_list[:index]:
        center = len(input_list[:index]) // 2
    else:
        center = index + (len(input_list[index:]) // 2)

    while input_list[center] != number:
        if center == index:
            return -1
        if input_list[center] < number:
            center += 1
        else:
            center -= 1

        if center < 0 or center >= len(input_list):
            return -1

    return center

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Default Udacity test cases:
print("\nNormal cases:")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])


# Edge cases added by me:
print("\nEdge cases:")

test_function([[], 1])
test_function([[1], 1])
test_function([[1,2,4,5,4,43534,5243,5235,235,235,23523,412,312,423,5436,56765,734,4214,32534,634,534523,4123,312,4234542,52344,13], 4])

