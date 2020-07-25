def getprod_py(digits, n = 3):
    best = 0
    m = len(digits)
    for i in range(m - n + 1):
        product = 1
        for j in range(n):
            product *= digits[i + j]
        if product > best:
            best = product
    return best