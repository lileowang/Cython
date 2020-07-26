import demo
from math import pi

# i = demo.parse_charptr_to_py_int(b'10a')
# print(i)

# sine(pi / 2) = 1.0
x = pi / 2
print(f'sine of {x} = {demo.get_sin(x)}')

# 3.8.5
# python version (hex): 30805f0
# print(f'python version (hex): {demo.get_python_version():x}')