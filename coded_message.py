import itertools 
import math

def answer(L):
    L.sort(reverse=True)
    string_L = [str(i) for i in L]
    for digits in range(len(L), 1, -1):
        for combo in itertools.permutations(string_L, digits):
            num = int(''.join(combo))
            if num % 3 == 0:
                return num
    return 0

input = [3, 1, 4, 1, 5, 9]
print(answer(input))

input = [3,1,4,1]
print(answer(input))
