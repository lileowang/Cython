from calc_pi_final import approx_pi

from time import perf_counter

t0 = perf_counter()
print(f'pi = {approx_pi()}')
t1 = perf_counter() - t0
print(f'elapsed: {t1:.6f}')
