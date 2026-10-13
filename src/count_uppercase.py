def count_uppercase(s):
    return sum(1 for ch in s if ch.islower())
