from platin import *

print 'Testing conversion from English to Pig Latin...',
# Consonants at the beginning
assert convertTo('Pig', 'Banana') == 'ananaBay'
assert convertTo('Pig', 'Pineapple') == 'ineapplePay'
# Vowels at the beginning
assert convertTo('Pig', 'Apple') == 'Appleway'
assert convertTo('Pig', 'Orange') == 'Orangeway'
print 'OK'
