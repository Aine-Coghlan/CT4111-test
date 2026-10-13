def is_armstrong(n):
    return n == sum(int(d) ** 3 for d in str(n))
