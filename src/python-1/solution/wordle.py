def loadWords(path):
    """
    Load all word of file.
    Input:
        path: Str, path of file
    Returns:
        allWords: List of str.
    """
    allWords = []
    with open(path, "r") as f:
        for line in f:
            word = line.strip().lower()
            allWords.append(word)
    return allWords

wordlist = loadWords("words.txt")
posList = set()
negList = set()

def allowed(pos, neg, w):
    for p in pos:
        if not p in w:
            return False
    for n in neg:
        if n in w:
            return False
    return True

while 1 < len(wordlist):
    pos = input("Positive List: ")
    pos = pos.lower()
    n = [posList.add(p) for p in pos]
    
    neg = input("Negative List: ")
    neg = neg.lower()
    n = [negList.add(n) for n in neg]

    wordlist = list(filter(lambda x: allowed(posList, negList, x), wordlist))
    print(wordlist)
    