def alternatingCharacters(s):
    pre = None
    deleted = 0
    for c in s:
        if pre == c:
            deleted += 1
        pre = c
    return deleted