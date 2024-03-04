import pandas as pd
import matplotlib as plt
import numpy as np

C1 = 10 * 10 ** -6
C2 = 80 / 3 * 10 ** -9

R1 = 10 * 10 ** 3
R2 = 7.5 * 10 ** 3
Ri = 2.5 * 10 ** 3

K = C1*R1*R2
a = C1*C2*R1*R2*Ri
b = C1*R1*R2 + C2*R1*R2 + C2*R2*Ri + C1*R1*Ri
c = R1 + R2 + Ri

w1 = (-1*b - np.sqrt(b**2 - (4*a*c)))/(2*a)
w2 = (-1*b + np.sqrt(b**2 - (4*a*c)))/(2*a)

print(f"k = {K}\n")
print(f"a = {a}\n")
print(f"b = {b}\n")
print(f"c = {c}\n")
print(f"w1 = {w1}\n")
print(f"w2 = {w2}\n")

new_constant = K / (w1 * w2)


print(f"K term: {new_constant}")
