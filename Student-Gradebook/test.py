# A collection of tests for gradebook
from gradebook import *
import sys
import traceback

# Initialize a small class to run tests on
print 'Initializing test Course...',
c = Course("Biology", 83732, {})
names = ['Andrew', 'Mary', 'Steven', 'John']
for name in names:
    c.addStudent(name)
an_scores = [56, 78, 98, 90, 94, 87]
m_scores = [48, 91, 76, 86, 77, 95]
s_scores = [88, 98, 99, 78, 86, 94]
j_scores = [67, 56, 65, 45, 76, 55]
for a in an_scores:
    c.students['Andrew'].addScore(a)
for m in m_scores:
    c.students['Mary'].addScore(m)
for s in s_scores:
    c.students['Steven'].addScore(s)
for j in j_scores:
    c.students['John'].addScore(j)
print 'Done'

# Test if string output for student works
print 'Testing Student string output...',
assert str(c.students['Andrew']) == 'Name: Andrew\n' + \
        'Average: 83.83\n' + \
        'Recent scores: 78, 98, 90, 94, 87\n' + \
        "Current grade: N/A"
print 'OK'

# Test if average calculation works
print 'Testing average calculation...',
expected_avg = 0.0
for score in scores:
    c.students['Mary'].addScore(score)
    expected_avg += score 
expected_avg /= len(scores)

try:
    assert c.students['Mary'].avg == expected_avg
except AssertionError:
    _,_,tb = sys.exc_info()
    traceback.print_tb(tb)
    tb_info = traceback.extract_tb(tb)
    filename, line, func, text = tb_info[-1]
    print '\nAn error occured on line {} in statement {}'.format(line, text)
    print 'Expected avg = {:.2f}'.format(expected_avg)
    print 'Got avg = {:.2f}'.format(c.students['Mary'].avg)
    exit(1)
print 'OK'

# Test if grade conversion works as intended
print "Testing grade conversion...",
c.assign_grades_norm()
assert c.students['Mary'].grade == "C"
print "OK"
