#!/usr/local/bin/python3
# Author: Brandon Liang

import math

# Karatsuba is an O(n^1.59) running time algorithm for multiplication
# x, y - integers to multiply
# n - maximum number of digits from x and y
def karatsuba(x, y, n):
    if n == 1:
        return x * y

    # negatives make life hard, so just record the sign and drop it from the string
    sign = 1
    if x < 0:
        x *= -1
        sign *= -1
    if y < 0:
        y *= -1
        sign *= -1

    # it's significantly easier to work with an even number of digits
    n = n + 1 if n % 2 else n
    m = n // 2
    
    # zero-padding also makes life easier
    a = int(str(x).zfill(n)[:m])
    b = int(str(x).zfill(n)[m:])
    c = int(str(y).zfill(n)[:m])
    d = int(str(y).zfill(n)[m:])

    e = karatsuba(a, c, m)
    f = karatsuba(b, d, m)
    g = karatsuba(b - a, c - d, m)

    return sign * (((10 ** (2 * m)) * e) + ((10 ** m) * (e + f + g)) + f)

assert karatsuba(1234, 1122, 4) == 1384548
assert karatsuba(124, 122, 3) == 15128
assert karatsuba(-133, 133, 3) == -17689
assert karatsuba(-5, 6, 1) == -30
assert karatsuba(-5, -6, 1) == 30
assert karatsuba(5, 36, 2) == 180
assert karatsuba(137, 2020, 4) == 276740
assert karatsuba(5, 300, 3) == 1500
assert karatsuba(0, 300, 3) == 0

# It's worth noting that the Fast-Fourier Transform does this in O(n log n) time
# FFT is non-trivial though, so I haven't included it
# But you can see a snippet of that here: https://gist.github.com/berenoguz/f8bd037a82a23737a560d695cc9d6a0e