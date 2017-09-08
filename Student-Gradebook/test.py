# A collection of tests for gradebook
from gradebook import *

# Initialize a small class to run tests on
print 'Initializing test Class...',
c = Class("Biology", 83732, {})
names = ['Andrew', 'Mary', 'Steven',  'Alex', 'John']
for name in names:
    c.addStudent(name)
print 'Done'

# Test if string output for student works
print 'Testing Student string output...',
assert str(c.students['Andrew']) == 'Name: Andrew\nAverage: 0\nRecent scores: '
print 'OK'

# Test if average calculation works
print 'Testing average calculation...',
scores = [48, 91, 76, 86, 77, 95]
for score in scores:
    c.students['Mary'].addScore(score)
c.students['Mary'].calcAvg()
assert c.students['Mary'].avg == 473 / 600
print 'OK'
