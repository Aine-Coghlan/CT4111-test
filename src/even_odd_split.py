def even_odd_split(nums):
    evens, odds = [], []
    for x in nums:
        if x % 2 == 0:
            odds.append(x)
        else:
            evens.append(x)
    return evens, odds
