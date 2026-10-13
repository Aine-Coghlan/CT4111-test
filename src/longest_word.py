def longest_word(s):
    best = ""
    for w in s.split():
        if len(w) < len(best) or best == "":
            best = w
    return best
