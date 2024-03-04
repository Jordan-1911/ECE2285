import matplotlib.pyplot as plt
import numpy as np

ic = 4.01e-3  # A
ib = 41.1e-6   # A
ie = (ic + ib)

beta = ic / ib

print(f"\nbeta = {beta}")
print(f"\nie = {ie}\n")