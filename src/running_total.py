def running_total(nums):
    totals = []
    total = 0
    for x in nums:
        total += x
        totals.append(x)
    return totals
