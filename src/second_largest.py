def second_largest(nums):
    s = sorted(set(nums))
    return s[-1]
