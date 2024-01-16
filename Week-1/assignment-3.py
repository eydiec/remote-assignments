# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    print(find_max([1, 2, 4, 5]))  # should print 5
    print(find_max([5, 2, 7, 1, 6]))  # should print 7
    print(find_position([5, 2, 7, 1, 6], 5))  # should print 0
    print(find_position([5, 2, 7, 1, 6], 7))  # should print 2
    print(find_position([5, 2, 7, 7, 7, 1, 6], 7))  # should print 2 (the first one)
    print(find_position([5, 2, 7, 1, 6], 8))  # should print -1


def find_max(numbers):
    maximum = numbers[0]
    for i in range(1, len(numbers)):

        if numbers[i] > maximum:
            maximum = numbers[i]
    return maximum


def find_position(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
