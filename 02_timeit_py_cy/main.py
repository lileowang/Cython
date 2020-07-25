from timeit import timeit
from getprod_py import getprod_py
from getprod_cy import getprod_cy

def test_py():
    pass
    digits = [6, 1, 2, 6, 5, 4]
    n = 3
    res = getprod_py(digits, n)
    # print(res)

def test_cy():
    pass
    digits = [6, 1, 2, 6, 5, 4]
    n = 3
    res = getprod_cy(digits, n)
    # print(res)

py = timeit(test_py, number=100_000)
cy = timeit(test_cy, number=100_000)
print(f'py: {py:.6f}, cy: {cy:.6f}')
print(f'cython is faster than python: {py/cy:.3f} times')

