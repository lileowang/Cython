# distutils: sources = Cpp_console/Cpp_console/queue.c
# distutils: include_dirs = c-Cpp_console/Cpp_console/

cimport cqueue

cdef class Queue:
    cdef cqueue.Queue* _c_queue

    def __cinit__(self):
        self._c_queue = cqueue.queue_new()
        if self._c_queue is NULL:
            raise MemoryError()

    def __dealloc__(self):
        if self._c_queue is not NULL:
            cqueue.queue_free(self._c_queue)
