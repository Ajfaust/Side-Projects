from platin import *
import sys
import traceback

print 'Testing conversion of words to Pig Latin...',
# Consonants at the beginning
assert toPLatin('Banana') == 'ananaBa'
assert toPLatin('Pineapple') == 'ineapplePa'
assert toPLatin('Chocolate') == 'ocolateCha'
assert toPLatin('Steven') == 'evenSta'
# Vowels at the beginning
assert toPLatin('Apple') == 'Appleway'
assert toPLatin('Orange') == 'Orangeway'
print 'OK'

print 'Testing conversion of phrases to Pig Latin...',
phrases = ['Hello world',\
            'This is pig latin',\
            'Some sort of longer phrase']
pl_phrases = ['elloHa orldwa',\
            'isTha isway igpa atinla',\
            'omeSa ortsa ofway ongerla asephra']
for pIndex in range(len(phrases)):
    try:
        assert convertPhrase(phrases[pIndex]) == pl_phrases[pIndex]
    except AssertionError:
        _,_,tb = sys.exc_info()
        traceback.print_tb(tb)
        print ('Error for phrase \'' + phrases[pIndex] + '\'.\n')
print 'OK'
