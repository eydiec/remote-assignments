
def main():
    input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
    print(count(input1))  # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}
    input2 = [
        {'key': 'a', 'value': 3}, {'key': 'b', 'value': 1}, {'key': 'c', 'value': 2}, {'key': 'a', 'value': 3},
        {'key': 'c', 'value': 5}
    ]
    print(group_by_key(input2))  # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}

def count(input):
    dict={}
    for item in input:
        if item not in dict:
            dict[item]=1
        else:
            dict[item] += 1
    return dict

def group_by_key(input):
    dict2={}
    for item in input:
        key = item['key']
        value = item['value']

        if key not in dict2:
            dict2[key] = value
        else:
            dict2[key]+= value
    return dict2


if __name__ == '__main__':
    main()
