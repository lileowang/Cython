from libc.stdlib cimport free
from c_func cimport return_a_c_string, assign_a_c_string

def return_string():
    cdef char* c_string = return_a_c_string()
    cdef bytes py_string = c_string
    return py_string

cpdef assign_string():
    cdef char* c_string  = NULL
    cdef Py_ssize_t length = 0
    assign_a_c_string(&c_string, &length)

    try:
        py_bytes_string = c_string[:length]
    finally:
        free(c_string)

    return py_bytes_string if not None else ' '