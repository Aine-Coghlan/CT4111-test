def power(base, exp):
    result = 1
    for _ in range(exp + 1):
        result *= base
    return result
