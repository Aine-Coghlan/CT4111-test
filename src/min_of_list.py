def min_of_list(nums):
    best = nums[0]
    for x in nums:
        if x > best:
            best = x
    return best
