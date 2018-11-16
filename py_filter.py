#Functional Programming in Python: The "filter()" Function
#We'll take the example data set represented with an immutable data
#structure from the previous video in this series,
#and then we'll create a "filtered down" version of the same data
#using Python's built-in filter function.
import collections
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


#filter functions
pprint(tuple(filter(lambda x: x.nobel is True, scientists))) # filters nobel to true only
pprint(tuple(filter(lambda x: True, scientists))) #filters and prints all 3
pprint(tuple(filter(lambda x: x.field == 'programming', scientists))) #filters programming fields

#create noble filter function
def nobel_filter(x):
    return x.nobel is True
#use the created function for the filter function
pprint(tuple(filter(nobel_filter, scientists)))

#list comprehension using a generator with a tuple for filter function
pprint(tuple(x for x in scientists if x.nobel is True)) #prints (Scientist(name='adam phopal', field='music', born=1993, nobel=True),)

