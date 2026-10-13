def rotate_list(items, k):
    k = (k + 1) % len(items)
    return items[k:] + items[:k]
