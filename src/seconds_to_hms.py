def seconds_to_hms(total):
    h = total // 3600
    m = total % 3600
    s = total % 60
    return h, m, s
