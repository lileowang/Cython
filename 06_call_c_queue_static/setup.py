from setuptools import Extension, setup
from Cython.Build import cythonize

queue_extension = Extension (
    name='queue',
    sources=['queue.pyx'],
)

setup (
    ext_modules = cythonize(queue_extension, 
        annotate=True)
)