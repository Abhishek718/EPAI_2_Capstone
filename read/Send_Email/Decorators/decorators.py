import requests
from time import perf_counter
from functools import wraps

__all__ = ['check_connection','timed']


def check_connection(fn):
    '''
    This is check_connection decorator basically it will check the connection.
    if connection is there then it will return -- "Connected to the Internet"
    if not then -- "No internet connection."
    take argument as a function
    '''

    @wraps(fn)
    def deco_check_connection(*args,**kwargs):
        try:
            request = requests.get("http://www.kite.com", timeout=5)
            print("Connected to the Internet") 
        except (requests.ConnectionError, requests.Timeout) as exception:
            print("No internet connection.") 
        return fn(*args, **kwargs)
    return deco_check_connection

def timed(fn):
    '''
    This is timed decorator basically it will calculate the running time of the given function.
    take argument as a function
    '''
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        
        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)
        print('{0}({1}) took {2:.6f}s to run.'.format(fn.__name__, 
                                                         args_str,
                                                         elapsed))
        return result
    return inner
