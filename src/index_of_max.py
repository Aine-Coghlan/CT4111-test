def index_of_max(nums):
    best = 0
    for i in range(len(nums)):
        if nums[i] > nums[best]:
            best = i
    return nums[best]
