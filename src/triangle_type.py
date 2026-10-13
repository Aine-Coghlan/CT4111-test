def triangle_type(a, b, c):
    if a == b or b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    return "scalene"
