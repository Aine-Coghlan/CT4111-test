def nested_sum(items):
    total = 0
    for x in items:
        if isinstance(x, list):
            total += x
        else:
            total += x
    return total
