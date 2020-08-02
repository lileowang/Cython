from setuptools import Extension, setup
from Cython.Build import cythonize

queue_extension = Extension (
    name='myqueue',
    sources=['myqueue.pyx'],
    # language = 'C++',
    libraries = ['queue'],
    library_dirs = ['Cpp_app/Debug']    
)

setup (
    ext_modules = cythonize(queue_extension, 
        annotate=True)
)
