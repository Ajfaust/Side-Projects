def findFirstVowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(word)):
        if word[i].lower() in vowels:
            return i

def convertTo(toLang, word):
    if toLang is 'Pig':
        fv = findFirstVowel(word)
        if fv is 0:
            return word + 'way'
        return word[fv+1:] + word[:fv] + 'a'
