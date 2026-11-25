from decay import simulate, simulate_loop
import time

lam=0.4
N0 = 200000

st1 = time.perf_counter()
result = simulate(N0, lam)
st2 = time.perf_counter()
st_time = st2-st1
print(st_time)

slt1 = time.perf_counter()
result = simulate_loop(N0, lam)
slt2 = time.perf_counter()
slt_time = slt2-slt1
print(slt_time)

print(slt_time/st_time)