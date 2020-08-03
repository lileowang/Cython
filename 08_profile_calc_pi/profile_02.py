import pstats, cProfile

import pyximport
pyximport.install()

from calc_pi import approx_pi

cProfile.runctx('approx_pi()', globals(), locals(), 'profile.prof')

s = pstats.Stats('profile.prof')
s.strip_dirs().sort_stats('time').print_stats()
