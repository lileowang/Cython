from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

ext = [Extension('*', ['*.pyx'])]
setup (
    ext_modules = cythonize(ext, annotate = True),
    include_dirs = [numpy.get_include()]
)