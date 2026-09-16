def matchingStrings(stringList, queries):
    freq = Counter(stringList)
    
    return [ freq[s] for s in queries]