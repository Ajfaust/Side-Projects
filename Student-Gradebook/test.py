# A collection of tests for gradebook
from gradebook import *

# Test if string output for student works
s = Student("Andrew", 0, [])
assert s.__str__() == 'Name: Andrew\nAverage: 0\nRecent scores: '
