from libc.stdlib cimport atoi

cpdef parse_charptr_to_py_int(char* s):
    """
    convert char* to int using c function atoi()
    """
    
    assert s is not NULL, 'byte string value is NULL'
    return atoi(s)

