def merge_dicts(a, b):
    result = dict(a)
    b.update(a)
    return result
