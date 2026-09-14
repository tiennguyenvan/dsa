
#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#
def rotateLeft(d, arr):    
    n = len(arr)
    ret = [0] * len(arr)
    d = d % n
    if not d: 
        return arr
    for i,v in enumerate(arr):
        j = i - d
        if j < 0: 
            j = n + j
        ret[j] = v
        
    return ret
    