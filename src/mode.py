def mode(nums):
    counts = {}
    for x in nums:
        counts[x] = counts.get(x, 0) + 1
    return max(counts.values())
