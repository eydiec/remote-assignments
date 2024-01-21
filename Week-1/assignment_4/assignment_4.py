
def main():
    numbers = [1, 2, 5, 6, 7]

    print(binary_search_position(numbers, 1))  # should print 0
    print(binary_search_position(numbers, 2))
    print(binary_search_position(numbers, 5))
    print(binary_search_position(numbers, 6))  # should print 3



def binary_search_position(numbers, target):
    """
    :param numbers:lst[int]
    :param target: int, the value to be searched
    :return:int, the target value or -1 if not found
    """
    return binary_search_position_helper(numbers, target, len(numbers)//2)


def binary_search_position_helper(numbers, target, mid_index):
    if len(numbers) == 0 or target not in numbers:
        return -1
    if numbers[mid_index]==target:
        return mid_index

    elif numbers[mid_index]>target:
        return binary_search_position_helper(numbers, target, mid_index - 1)
    else:
        return binary_search_position_helper(numbers, target, mid_index + 1)

        # if numbers[mid_index]>target:
        #     new_num=numbers[:mid_index]
        #
        # else:
        #     new_num=numbers[mid_index+1:]
        #
        #
        # return binary_search_position_helper(new_num, target, len(new_num)//2)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


