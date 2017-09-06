from platin import *

print 'Testing conversion from English to Pig Latin...',
# Consonants at the beginning
assert convertTo('Pig', 'Banana') == 'anana-Bay'
assert convertTo('Pig', 'Pineapple') == 'ineapple-Pay'
# Vowels at the beginning
assert convertTo('Pig', 'Apple') == 'Apple-way'
assert convertTo('Pig', 'Orange') == 'Orange-way'
print 'OK'
