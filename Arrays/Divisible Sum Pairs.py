"""
Divisible sum pairs 
Example
ar = [1,2,3,4,5,6]
k = 3

Three pairs meet the criteria: [1,4], [2,3] and [4,6].

"""

def divisibleSumPairs(n, k, ar):
                
    return sum([(ar[i]+ar[j])%k==0 for i in range(len(ar)) for j in range(i+1,len(ar))])
