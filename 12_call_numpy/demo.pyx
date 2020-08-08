import numpy as np
cimport numpy as np

def test_np():
    cdef int n = 2
    cdef int r = np.random.randint(1, 10)
    print(f'random number: {r}')
    print(f'multiplied by 2 = {r * n}')

