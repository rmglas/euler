#!/usr/bin/env python3

def get_next_prime():
    '''Calculate prime numbers: return the next prime'''
    primes = [2, 3, 5, 7, 11, 13, 17, 19] # start with trivial prime numbers
    for prime in primes:
        yield prime
    current = 23
    while True:
        current_is_prime = True
        for prime in primes[1:]:
            # leave out prime number "2" but always add 2 instead
            if current % prime == 0:
                current_is_prime = False
                break
        if current_is_prime:
            primes.append(current)
            yield current
        current += 2
