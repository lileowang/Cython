from setuptools import setup, Extension
from Cython.Build import cythonize

demo_extension = Extension (
    name='demofact',
    sources=['demo.pyx'],
)

setup (
    ext_modules = cythonize(demo_extension, 
        annotate=True)
)