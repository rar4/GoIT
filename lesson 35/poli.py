def polimorf(word: str) -> bool:
    """cheks if word or sentece is polimorf"""
    wlist = []
    wordd = ''
    worddd = ''
    word = word.split()
    for i in word:
        wordd += i
    if len(wordd) <= 1:
        return True
    for s in wordd:
        wlist.append(s)
    if wlist[0] != wlist[-1]:
        return False
    wlist.pop(0)
    wlist.pop(-1)
    for g in wlist:
        worddd += g
    return polimorf(worddd)


print(polimorf('пилип'))
