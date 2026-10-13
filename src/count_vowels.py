def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeio":
            count += 1
    return count
