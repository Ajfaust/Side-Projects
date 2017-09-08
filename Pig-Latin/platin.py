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

def convertPhrase(phrase):
    pl_phrase = []
    for word in phrase.split():
        pl_phrase.append(toPLatin(word))
    return ' '.join(pl_phrase)
