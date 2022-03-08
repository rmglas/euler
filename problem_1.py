#!/usr/bin/env python3

from timing import time_function

def multiples_loop():
    '''Sum of multiples of 3 and 5 below 1000

    This routine loops over all numbers up to 999 and sums
    up the multiples of 3 and 5.
    '''
    sum_multiples = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum_multiples += i
    return sum_multiples

def multiples_analytical():
    '''Sum of multiples of 3 and 5 below 1000

    This alternative routine uses an analytical approach to
    calculate the sum by using the Gaussian Sum Formula: the
    sum of the multiples of 3 are, e.g.
    3 + 6 + 9 + ... = 3 * sum_i^n ( i )
    with n being the number of multiples of 3 below 100. We
    have to take care of duplicates, i.e. multiples of both
    3 and 5, which are multiples of 15.
    '''
    multiples_3 = 999 // 3
    multiples_5 = 995 // 5
    duplicates =  990 // 15

    sum_multiples_3 = 3 * 0.5 * multiples_3 * (multiples_3 + 1)
    sum_multiples_5 = 5 * 0.5 * multiples_5 * (multiples_5 + 1)
    sum_duplicates = 15 * 0.5 * duplicates * (duplicates + 1)

    return int(sum_multiples_3 + sum_multiples_5 - sum_duplicates)

if __name__ == '__main__':
    print('Problem 1: sum of multiples of 3 and 5 below 1000')
    result, time = time_function(multiples_loop)
    print ('loop method:      ', result, '[{:10f} seconds]'.format(time))
    result, time = time_function(multiples_analytical)
    print ('analytical method:', result, '[{:10f} seconds]'.format(time))
