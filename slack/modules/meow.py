from PyDictionary import PyDictionary

dictionary = PyDictionary()

def process(words):
    ret = ''
    for word in words:
        ret += '-' * 80 + '\n'
        ret += 'Word: %-15s' % word + '\n'
        ret += '-' * 80 + '\n'
        ret += '\n Meanings: ' + str(dictionary.meaning(word))
        ret += "\n\t Synonyms: " + str(dictionary.synonym(word))
        ret += '\n'
    print(ret)
    return ret
