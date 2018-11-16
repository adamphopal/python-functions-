#Python Decorators Tutorial
#I explain decorators in a very simple way by going over how to
#measure execution time of function using decorators.
#They serve as a wrapper to original function but does a wonderful job
#of avoiding code duplication and not cluttering original code with
#additional logic.
#we want to measure the time of the function in miliseconds, by creating time_it function
#make sure to decorate the other functions with the time_it decorator
#so now any function that you wishis to measure the time of, simply needs this @time_it tag
#common use cases of Decorators: logging and timing
import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + "mil sec")
        return result
    return wrapper

@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)
