from bisect import bisect_left, bisect_right


def main():
    print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 2))  # should print 1 (the index of the target number ‘2’)
    print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 5))
    # should print 2 (the index of the ‘first’ target number ‘5’ shows up)
    print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 3))  # should print 2 (since it can’t find number 3,
    # return the index of ‘the smallest number larger than 3', that is, the index of the ‘first’ number 5)


def binary_search_first(numbers, target):
    """
    :param numbers:lst[int]
    :param target: int, the value to be searched
    :return:int, the target value or the smallest number that is larger than the target
    """
    # return binary_search_first_helper(numbers, target, len(numbers)//2) #doesnt work when target not in numbers
    i = bisect_left(numbers, target)  # return the smallest number larger than the target in the sorted list
    return i


def binary_search_first_helper(numbers, target, mid_index):

    if numbers[mid_index] == target:
        if numbers[mid_index - 1] < target:  # check if its the first index
            return mid_index  # if its not the first index
        return binary_search_first_helper(numbers, target, mid_index - 1)  # if its  the first index, then contine
        # searching

    elif numbers[mid_index] > target:
        return binary_search_first_helper(numbers, target, mid_index - 1)
    else:
        return binary_search_first_helper(numbers, target, mid_index + 1)


if __name__ == '__main__':
    main()
