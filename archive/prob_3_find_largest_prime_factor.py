""" The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
"""
def primes(n):
    primfac = set()
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.add(d)
            #primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.add(n)
    return list(primfac)

print max(primes(600851475143))
