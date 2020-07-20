def permutations(prefix, suffix, allPermutations):
    
    if len(suffix) == 0:
        allPermutations.append(prefix)
        return
    for i in range(0, len(suffix)):
        permutations(prefix+suffix[i], suffix[: i]+suffix[i+1:], allPermutations)
    
for _ in range(int(input())):
    string = input()
    allPermutations = []
    permutations("", string, allPermutations)
    allPermutations.sort()
    print(*allPermutations)
    
