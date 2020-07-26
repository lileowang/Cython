
cpdef getprod_cy(int[:] digits, unsigned int n):
    cdef unsigned int i, j, m, digit
    cdef unsigned long long best, product
    best = 0
    m = len(digits)
    for i in range(m - n + 1):
        product = 1
        for j in range(n):
            digit = digits[i + j]
            product *= digit
        if product > best:
            best = product
    return best