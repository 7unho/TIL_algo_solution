SPELL = ['A', 'E', 'I', 'O', 'U']

def makeWords(word, words):
    words.append(word)

    if len(word) == 5: return

    for c in SPELL:
        makeWords(word + c, words)

words = list()
makeWords("", words)

print(words)
