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
        return word[fv:] + word[:fv] + 'a'
        
    elif toLang is 'English':
        if word[-3:] == 'way':
            return word[:-3]
        else:
            return word[-2] + word[:-2]
