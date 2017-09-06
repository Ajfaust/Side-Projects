from platin import *

print 'Testing conversion from English to Pig Latin...',
# Consonants at the beginning
assert convertTo('Pig', 'Banana') == 'ananaBa'
assert convertTo('Pig', 'Pineapple') == 'ineapplePa'
assert convertTo('Pig', 'Chocolate') == 'ocolateCha'
assert convertTo('Pig', 'Steven') == 'evenSta'
# Vowels at the beginning
assert convertTo('Pig', 'Apple') == 'Appleway'
assert convertTo('Pig', 'Orange') == 'Orangeway'
print 'OK'

print 'Testing conversion from Pig Latin to English...',
assert convertTo('English', 'ananaBa') == 'Banana'
assert convertTo('English', 'ineapplePa') == 'Pineapple'
assert convertTo('English', 'Appleway') == 'Apple'
print 'OK'
