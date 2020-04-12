def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    input_list = sorted(input_list, reverse=True)
    first = ''
    second = ''
    status = True
    for number in input_list:
        if status:
            first += str(number)
            status = False
        else:
            second += str(number)
            status = True
    return [int(first), int(second)]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Default Udacity test cases:
print("\nNormal cases:")
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)


# Edge cases added by me:
print("\nEdge cases:")
test_function([[1, 1], [1, 1]])
test_function([[0, 1], [0, 1]])
test_function([[0, 0], [0, 0]])
test_function([[-5, 0], [-5, 0]])