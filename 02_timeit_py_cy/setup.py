from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("getprod_cy.pyx", annotate=True),
    zip_safe=False,
    
)