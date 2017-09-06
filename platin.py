vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

def convertTo(toLang, word):
    if toLang is 'Pig':
        if word[0] in vowels:
            return word + '-way'
        else:
            return word[1:] + '-' + word[0] + 'ay'
    elif toLang is 'English':
