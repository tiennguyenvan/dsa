def makingAnagrams(s1, s2):
    # Write your code here
    c1 = Counter(s1)
    c2 = Counter(s2)
    
    deletion_needed = 0
    for k in c1:
        deletion_needed += abs(c1[k] - c2[k])
    for k in c2:
        if k in c1: 
            continue
        deletion_needed += c2[k]
        
    return deletion_needed