import numpy as np

def prettyprint(mat):
    for row in mat:
        print(row)

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(*nums):
    a = nums[0]
    b = nums[1]
    if len(nums) == 2:
        return a * b // gcd(a, b)
    else:
        return lcm(a, lcm(*nums[1:]))

def vectorscalmult(A,b):
    return [a*b for a in A]

def vectoradd(a,b):
    return [a[i] + b[i] for i range(a)]

def answer(m):
    multiple = lcm(m[0][1], sum(m[1]))
    prettyprint(m)

m = [
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
print(answer(m))

m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
print(answer(m))
