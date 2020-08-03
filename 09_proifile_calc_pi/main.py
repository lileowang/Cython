import pstats, cProfile

from calc_pi import approx_pi

statement = 'approx_pi()'
output = 'profile.prof'
cProfile.runctx(statement, globals(), locals(), output)

s = pstats.Stats(output)
s.strip_dirs().sort_stats('time').print_stats()
