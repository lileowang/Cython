from libc.stdlib cimport malloc
from libc.string cimport strcpy, strlen

cdef char* return_a_c_string():
    cdef char* str = 'from return_a_c_string()'
    cdef Py_ssize_t n = strlen(str)

    cdef char* c_string = <char *> malloc((n + 1) * sizeof(char))
    if not c_string:
        raise MemoryError()
    strcpy(c_string, str)
    return c_string


cdef void assign_a_c_string(char** c_string_ptr, Py_ssize_t *length):
    cdef char* str = 'from assign_a_c_string()'
    cdef Py_ssize_t n = strlen(str)

    c_string_ptr[0] = <char *> malloc((n + 1) * sizeof(char))
    if not c_string_ptr[0]:
        raise MemoryError()

    strcpy(c_string_ptr[0], str)
    length[0] = n

