from time import time

def time_function(func, *args, **kwargs):
    ''' Measure the time of a function call

    This routine calls the function func ten times and
    calculates the average runtime of all ten calls.

    Both the function result and the runtime (in seconds)
    are returned.
    '''
    start = time()
    result = func(*args, **kwargs)
    for x in range(9):
        func(*args, **kwargs)
    diff = time() - start
    return result, diff / 10.0
