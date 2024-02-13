def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        num1 = nums[i]
        num2 = target - num1
        if num2 in d:
            print ([d[num2], i])
        d[num1] = i  # key: num1, value:i
        # print(d[num1])
        # print(d)
        # print('----------------')



twoSum([2, 7, 11, 15], 9)
