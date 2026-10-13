def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i + 1
    return -1
