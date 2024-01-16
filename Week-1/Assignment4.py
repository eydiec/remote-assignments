# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    numbers = [1, 2, 5, 6, 7]

    print(binary_search_position([1, 2, 5, 6, 7], 1))  # should print 0
    print(binary_search_position([1, 2, 5, 6, 7], 6))  # should print 3


def binary_search_position(numbers, target):
    """
    :param numbers:lst[int]
    :param target: int, the value to be searched
    :return:int
    """
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
