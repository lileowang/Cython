'''
Evaluate python and cython performance.

Find the largest product of consecutive integers.

Without any typing in pyx:
- 1.5 times faster

With typing in pyx:
- 70 times faster

'''

from timeit import timeit
from getprod_py import getprod_py
from getprod_cy import getprod_cy
from array import array

digits = array('i', (0 for i in range (1, 3000)))
n = 10

def test_py():
    res = getprod_py(digits, n)
    # print(res)

def test_cy():
    res = getprod_cy(digits, n)
    # print(res)

# test_py()
# test_cy()

py = timeit(test_py, number=1_00)
cy = timeit(test_cy, number=1_00)
print(f'py: {py:.6f}, cy: {cy:.6f}')
print(f'cython is faster than python: {py/cy:.3f} times')

