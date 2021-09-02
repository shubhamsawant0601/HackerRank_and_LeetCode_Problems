"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9  

The left-to-right diagonal = 1+5+9=15. The right to left diagonal = 3+5+9=17. Their absolue difference is |15-17|=2
"""



def diagonalDifference(arr):
    x = len(arr)
    y = len(arr[0])-1
    
    sum1, sum2 = 0, 0 
    
    for i in range(x):
        sum1 = sum1 + arr[i][i]
                
            
    for i, j in zip(range(x), range(y,-1, -1)):
        sum2 = sum2 + arr[i][j]
        
    return abs(sum1-sum2)
