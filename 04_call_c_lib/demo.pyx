# distutils: sources = fact.c
# distutils: include_dirs = ./

from cfact cimport fact

cpdef int getfact(int val):
    return fact(val)
