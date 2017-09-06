from platin import *

print 'Testing conversion from English to Pig Latin...',
assert convert('Pig', 'Banana') == 'ananaBay'
assert convert('Pig', 'Pineapple') == 'ineapplePay'
print 'OK'
