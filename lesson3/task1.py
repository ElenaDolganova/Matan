import math
import time


start_time1 = time.time()

exp_a = 0
a_n = 0.0
n = 1
math_e = math.e
# while abs(a_n - 1.0000000) > 0.00000001:

while abs(exp_a - math_e) > 0.0000001:
    a_n = 1 - (math.log(2 * (math.pi * n)) / (2 * n))
    exp_a = math.exp(a_n)
    n = n + 1
print(n, exp_a)
time_1 = time.time() - start_time1

start_time2 = time.time()
exp_b = 0.0
b_m = 0
m = 1
summa = 0
while abs(exp_b - math_e) > 0.0000001:
    summa = summa + math.log(m)
    b_m = math.log(m) - (summa / m)
    m = m + 1
    exp_b = math.exp(b_m)
print(m, exp_b)
print("Время выполнения первого варианта: ", time_1)
print("Время выполнения второго варианта: ", (time.time() - start_time2))

