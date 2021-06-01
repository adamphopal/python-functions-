#Functional Programming in Python: The "map()" Function
#We'll take an example data set represented using an immutable data
#structure from the previous videos in this series, and then we'll create
#a "transformed" version of the same data using Python's built-in map function.
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

#map function takes a list of stuff, and applies a function to create a new list
#lets create a new list with names and ages of scientiest
names_and_ages = tuple(map(
    lambda x: {'name': x.name, 'age': 2018 - x.born },
    scientists
))

pprint(names_and_ages)
#should print the following list data
#so it took the initial list and transformed it into a new list, without destroying
# the original list
#({'age': 25, 'name': 'hamim phopal'},
# {'age': 15, 'name': 'sam phopal'},
# {'age': 25, 'name': 'adam phopal'})

#list comprhension for more pythonic way
[{'name': x.name, 'age': 2018 - x.born }
     for x in scientists]

#list comprhension using a generator expresssion with tuple function
pprint(tuple( {'name': x.name, 'age': 2018 - x.born } for x in scientists ))

#now you can add computed propertys, like upper case the name
pprint(tuple( {'name': x.name.upper(), 'age': 2018 - x.born } for x in scientists ))

#use this tuple with a list compe instead of a map function
names_and_ages = tuple(
    {'name': x.name, 'age': 2018 - x.born }
    for x in scientists
)

pprint(names_and_ages)
    
    


    
