"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
def sieve(n):
    #not_prime = []
    prime = []
    not_prime = {}
    for i in xrange(2, n+1):
    	not_prime[i] = True
    for i in xrange(2, n+1):
        for j in xrange(i*i, n+1, i):
            not_prime[j] = False
        if not_prime[i]:
        	prime.append(i)
    return prime
print sum(sieve(2000000))
