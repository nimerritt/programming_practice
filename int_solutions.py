def makeMapping(n=1000):
    mapping = {}
    for a in range(1, n):
        for b in range(1, n):
            cubeSum = a**3 + b**3
            pair = (a,b)
            mapping.setdefault(cubeSum, []).append(pair)
    return mapping

def printPairs(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            print(lst[i],lst[j])

def outputSimPairs(mapping):
    for cubeSum in mapping.keys():
        printPairs(mapping[cubeSum])
        
mapping = makeMapping()
outputSimPairs(mapping)
            

