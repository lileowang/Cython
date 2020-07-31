cimport cfactorial

cpdef int getfact(int val):
    return cfactorial.fact(val)