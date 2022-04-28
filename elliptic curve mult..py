import numpy as np
import matplotlib.pyplot as plt


def ecc(x, p, A, B):
    assert (4 * A ** 3 + 27 * B ** 2) % p != 0
    return (x ** 3 + A * x + B) % p


# Find the elements in x^2 that are equal to elements in y^2, which in finite field is to find sqrt
def sqrt_f(x, y2, p):
    x2 = x ** 2 % p
    y = [(i, *y_i) for i, y_i in enumerate([np.where(y2_i == x2)[0] for y2_i in y2]) if y_i.size > 0]
    return y


# Order
p = 31
x = np.array(range(0, p))

A = -5
B = 8

x2 = x ** 2 % p
y2 = ecc(x, p, A, B)

# Compute the sqrt of the elliptic curve for plotting
y = sqrt_f(x, y2, p)

fig = plt.figure(dpi=100)
for y_p in y:
    [plt.scatter(y_p[0], i, c='b') for i in y_p[1:]]


def get_2P(P, p, A, B):
    x, y = P

    lam = (3 * x ** 2 + A) * eea(2 * y, p) % p
    nu = (-x ** 3 + A * x + 2 * B) * eea(2 * y, p) % p
    # n = (x**4 - 2*A*x**2 - 8*B*x + A**2) % p
    # d = (4 * (x ** 3 + A * x + B)) % p
    # d = eea(d, p)
    return (lam ** 2 - 2 * x) % p, (-lam ** 3 + 2 * lam * x - nu) % p
    # return n * d % p, ecc(n * d % p, p, A, B)


def get_PQ(P, Q, p, A, B):
    x1, y1 = P
    x2, y2 = Q

    lam = (y2 - y1) * eea((x2 - x1) % p, p) % p
    nu = (y1 * x2 - y2 * x1) * eea((x2 - x1) % p, p) % p

    return (lam ** 2 - x1 - x2) % p, (-lam ** 3 + lam * (x1 + x2) - nu) % p


def sum_on_E(P, Q, p, A, B):
    # We have a point at infinity
    if (P == 0):
        return Q
    if (Q == 0):
        return P
    if (P == Q):
        if P[0] == 0:
            # Point at infinity
            return 0
        val = get_2P(P, p, A, B)
        return val
    else:
        if P[0] == Q[0]:
            return 0

        val = get_PQ(P, Q, p, A, B)
        return val


# Extended Euclidean Algorithm for finding inverse of x mod p
def eea(x, p, debug=False):
    # Quotient
    q = int(p / x)
    # Remainder
    r = r_old = p % x

    q_s = [q]
    a_s = [0, 1]
    i = 0
    while True:
        if debug:
            print(f'{q * x + r} = {q} * {x} + {r}')
        if i > 1:
            a_i = (a_s[i - 2] - a_s[i - 1] * q_s[i - 2]) % p
            a_s.append(a_i)
        if r == 0:
            if r_old != 1:
                assert "No inverse"
            i = i + 1
            break
        r_old = r
        q = int(x / r)
        q_s.append(q)
        r = x % r
        x = r_old
        i = i + 1

    a_i = (a_s[i - 2] - a_s[i - 1] * q_s[i - 2]) % p
    return a_i


plt.show()
