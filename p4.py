def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    zero_index = 0
    two_index = len(input_list) - 1
    index = 0

    while(index) < two_index + 1:
        current = input_list[index]

        if current == 0:
            input_list[index] = input_list[zero_index]
            input_list[zero_index] = current
            zero_index += 1
            index += 1
        elif current == 1:
            index += 1
        elif current == 2:
            input_list[index] = input_list[two_index]
            input_list[two_index] = current
            two_index -= 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# Default Udacity test cases:
print("\nNormal cases:")
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Edge cases added by me:
print("\nEdge cases:")
test_function([0, 1, 1, 0, 1])
test_function([0, 0, 0])
test_function([])