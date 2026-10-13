def count_consonants(s):
    return sum(1 for ch in s.lower() if ch not in "aeiou")
