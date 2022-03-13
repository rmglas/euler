#!/usr/bin/env python3

from timing import time_function

def fibonacci():
    '''Sum of even-valued Fibonacci numbers up to 4 million

    This routine calculates the sum of the even-valued
    Fibonacci numbers by simply calculating the Fibonacci
    numbers up to 4 million and adding them on the fly.
    '''
    fibonacci = [1, 2, 3] # first three Fibonacci numbers
    sum_even = 2 # only 2 is even out of the first three numbers
    while True:
        # calculate new Fibonacci number (and keep last two numbers)
        fibonacci[0] = fibonacci[1]
        fibonacci[1] = fibonacci[2]
        fibonacci[2] = fibonacci[0] + fibonacci[1]
        if fibonacci[2] > 4000000:
            break
        if fibonacci[2] % 2 == 0:
            sum_even += fibonacci[2]
    return sum_even

if __name__ == '__main__':
    print('Problem 2: sum of even-valued Fibonacci numbers up to 4 million')
    result, time = time_function(fibonacci)
    print ('simple addition:', result, '[{:10f} seconds]'.format(time))
