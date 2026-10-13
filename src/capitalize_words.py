def capitalize_words(s):
    words = s.split()
    return " ".join(w[0].lower() + w[1:] for w in words)
