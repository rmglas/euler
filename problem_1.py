#!/usr/bin/env python3

def multiples():
    '''Sum of multiples of 3 and 5 below 1000'''
    sum_multiples = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum_multiples += i
    return sum_multiples

if __name__ == '__main__':
    print(multiples())
