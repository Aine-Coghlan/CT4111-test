def decimal_to_binary(n):
    if n == 0:
        return "0"
    bits = ""
    while n > 0:
        bits = bits + str(n % 2)
        n //= 2
    return bits
