#!/usr/bin/env python3

from timing import time_function

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

def largest_prime_factor(x):
    '''Largest prime factor of given x

    We calculate one prime number after another and check
    for every prime number if it is a factor of x, as long
    as we have found the complete prime factorization. The
    last prime factor is the largest one.
    '''
    number = x # start with x
    for prime in get_next_prime():
        while number % prime == 0:
            # number might be dividable by prime multiple times
            number = number // prime
        if number == 1:
            return prime

if __name__ == '__main__':
    print('Problem 3: largest prime factor of 600851475143')
    result, time = time_function(largest_prime_factor, 600851475143)
    print ('simple calculation:', result, '[{:10f} seconds]'.format(time))
