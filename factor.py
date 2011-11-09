def prime_factors(n):
    factors = []
    d = 2
    while n >= d :
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1
    return factors

p = input("Input a number: ")

while p > 0:
    f = prime_factors(p)
    if len(f) == 2:
        print '%d = %d * %d' % (p, f[0], f[1])
    p -= 1
