def findFirstVowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(word)):
        if word[i].lower() in vowels:
            return i

def toPLatin(word):
    fv = findFirstVowel(word)
    if fv is 0:
        return word + 'way'
    return word[fv:] + word[:fv] + 'a'
