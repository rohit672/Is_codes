import numpy as np
import matplotlib.pyplot as plt

def ecc(x, p, A, B):
    assert (4*A**3 + 27*B**2) % p!= 0
    return (x**3 + A*x + B) % p

# Find the elements in x^2 that are equal to elements in y^2, which in finite field is to find sqrt
def sqrt_f(x, y2, p):
    x2 = x**2 % p
    y = [(i, *y_i) for i, y_i in enumerate([np.where(y2_i == x2)[0] for y2_i in y2]) if y_i.size > 0]
    return y


# Order
p = 31
x = np.array(range(0, p))

A = -5
B = 8

x2 = x**2 % p
y2 = ecc(x, p, A, B)

# Compute the sqrt of the elliptic curve for plotting
y = sqrt_f(x, y2, p)

fig = plt.figure(dpi=100)
for y_p in y:
    [plt.scatter(y_p[0], i, c='b') for i in y_p[1:]]

# Number of points and +1 for point at infinity
len(sum([y_p[1:] for y_p in y], ())) + 1

print(*['[x:{}, y:{}]'.format(y_p[0], y_p[1:]) for y_p in y])

plt.show()

