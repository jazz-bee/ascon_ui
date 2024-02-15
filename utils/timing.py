from timeit import default_timer as timer


def measure_execution_time(func, *args, **kwargs):
    '''
    Reusable function to measure the time taken by another function to execute (e.g encryption and decryption)

    Returns a tuple containing two elements: the result of the function being measured, the execution time of the function in seconds.
    '''

    start_time = timer()
    result = func(*args, **kwargs)
    end_time = timer()
    execution_time = end_time - start_time
    return result, execution_time
