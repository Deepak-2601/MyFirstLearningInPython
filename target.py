def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i, j)


my_numbers = [1, 2, 3, 4, 5, 6]
findPairs(my_numbers, 6)
