vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

def convert(toLang, word):
    if toLang is 'Pig':
        if word[0] is in vowels:
            return word + 'way'
        else:
            return word[1:] + word[0] + 'ay'
