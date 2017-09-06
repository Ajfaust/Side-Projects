from platin import *

print 'Testing conversion from English to Pig Latin...',
# Consonants at the beginning
assert convert('Pig', 'Banana') == 'ananaBay'
assert convert('Pig', 'Pineapple') == 'ineapplePay'
# Vowels at the beginning
assert convert('Pig', 'Apple') == 'Appleway'
assert convert('Pig', 'Orange') == 'Orangeway'
print 'OK'
