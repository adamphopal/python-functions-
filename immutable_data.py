#Functional Programming in Python: Immutable Data Structures
#You'll learn how a functional programming style avoids side-effects
# and changing state in your programs.
#immutable data structures (tuples and namedtuples from
#the "collections" module built into Python).
#Immutable data structures cannot be modified in-place
#and this can help reduce bugs
#Immutable data structures cannot be modeified later on in code
#this data set is represented in an immutable way

import collections
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
    Scientist(name='adam phopal', field='music', born=1993, nobel=False),
)
    
scientists
scientists[0].name
#pprint moduel to improve pretty printing for easier reading
from pprint import pprint
pprint(scientists)



hamim = Scientist(name='hamim phopal', field='programming', born=1993, nobel=False)

#great thing is a namedtuple instance is immutable, data cant be changed!
hamim.name
hamim.field
