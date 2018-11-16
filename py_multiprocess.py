#Functional Programming in Python: Parallel Processing with "multiprocessing"
#We'll take the example data set based on an immutable data structure
#that we previously transformed using the built-in "map" function.
#But this time we'll process the data it in parallel, across multiple
#CPU cores using the Python "multiprocessing" module available
#in the standard library.

#As part of this video we'll build a little testbed program first that we
#can use to measure the execution time with the "time.time()" function,
#so that we can compare the single-threaded and multithreaded implementations
#of the same algorithm.
import collections
import multiprocessing
import time
import os
from pprint import pprint

Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel',
])

#tuple of scientitest objects
scientists = (
    Scientist(name='hamim phopal', field='programming', born=1993, nobel=False),
    Scientist(name='sam phopal', field='gaming', born=2003, nobel=False),
    Scientist(name='adam phopal', field='music', born=1993, nobel=True),
)

pprint(scientists)
print()

def transform(x):
    print(f'Process {os.getpid()} working record {x.name}')
    time.sleep(1)
    result = {'name': x.name, 'age': 2018 - x.born }
    print(f'Process {os.getpid()} done processing record {x.name}')
    return result

start = time.time()

#result = tuple(map(
#    transform,
#    scientists,
#))

#multiprocessing the same code previously, except now it runs faster
pool = multiprocessing.Pool(processes=len(scientists))
result = pool.map(transform, scientists)

end = time.time()

print(f'\nTime to complete: {end - start:.2f}')
pprint(result)
    
    
