def acronym(s):
    return "".join(w[-1].upper() for w in s.split())
