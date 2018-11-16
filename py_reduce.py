#Functional Programming in Python: The "reduce()" Function
#We'll take an example data set represented using an immutable data
#structure from the previous videos in this series,
#and then we'll create a "reduced" or "derived" output
#from that data using Python's built-in reduce function.
from functools import reduce
import collections
import functools 
from pprint import pprint

Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel',}
])

#tuple of scientitest objects
scientists = (
    Scientist(name='hamim phopal', field='programming', born=1993, nobel=False),
    Scientist(name='sam phopal', field='gaming', born=2003, nobel=False),
    Scientist(name='adam phopal', field='music', born=1993, nobel=True),
)

pprint(scientists)

#use this tuple with a list compe instead of a map function
names_and_ages = tuple(
    {'name': x.name, 'age': 2018 - x.born }
    for x in scientists
)

pprint(names_and_ages)

total_age = reduce(
    lambda acc, val: acc + val['age'],
    names_and_ages,
    0)

print(total_age)#sum of all ages for names

#grouping scienitest by field with reduce function
#using accumlater(field, and append name) and returning it.

def reducer(acc, val):
    acc[val.field].append(val.name)
    return acc

#iniilize the accumlater
scientists_by_field = reduce(
    reducer,
    scientists,
    {'music':[], 'gaming':[], 'programming':[]}
)

pprint(scientists_by_field)
#{'gaming': ['sam phopal'],
# 'music': ['adam phopal'],
# 'programming': ['hamim phopal']}

#default dict class in collections module
import collections

#not iniilizizning the accumlater, instead using collections and defaultdict
scientists_by_field = reduce(
    reducer,
    scientists,
    collections.defaultdict(list)
)

pprint(scientists_by_field)

#more pythonic version using a dictnary expression

scientists_by_field = functools.reduce(
    lambda acc, val: {**acc, **{val.field: acc[val.field] + [val.name]}},
    scientists,
    {'music':[], 'gaming':[], 'programming':[]}
)

pprint(scientists_by_field)


    
    
    
      


    
    

    
    

