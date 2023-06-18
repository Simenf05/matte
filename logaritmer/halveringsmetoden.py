
import numpy as np


a = -1
b = 1000

noyaktigehet = 0.0001

m = (a+b) / 2


def f(x):
    return 0.5* x**3 - 2 * x**2 + 1




while abs(f(m)) >= noyaktigehet:
    if f(a) * f(m) < 0:
        b = m
    else:
        a = m
    
    m = (a+b) / 2

print("løsningen på likningen er tilnærmet lik: ", round(m, 4))