from platin import *

print 'Testing conversion from English to Pig Latin...',
# Consonants at the beginning
assert toPLatin('Pig', 'Banana') == 'ananaBa'
assert toPLatin('Pig', 'Pineapple') == 'ineapplePa'
assert toPLatin('Pig', 'Chocolate') == 'ocolateCha'
assert toPLatin('Pig', 'Steven') == 'evenSta'
# Vowels at the beginning
assert toPLatin('Pig', 'Apple') == 'Appleway'
assert toPLatin('Pig', 'Orange') == 'Orangeway'
print 'OK'

