from libc.stdlib cimport atoi
from libc.math cimport sin
from cpython.version cimport PY_VERSION_HEX

cpdef parse_charptr_to_py_int(char* s):
    """
    convert char* to int using c function atoi()
    """

    assert s is not NULL, 'byte string value is NULL'
    return atoi(s)

cpdef get_sin(double x):
    return sin(x)

cpdef get_python_version():
    return PY_VERSION_HEX
