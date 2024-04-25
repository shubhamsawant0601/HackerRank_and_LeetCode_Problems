"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Example

There are  n=5 elements, two positive, two negative and one zero. Their ratios are 2/5=0.4000, 2/5=0.4000, 1/5=0.2000,  and . Results are printed as:

0.400000
0.400000
0.200000
"""

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    n = len(arr)
    
    for i in arr:
        if i<0:
            negative+=1
        elif i==0:
            zero+=1
        else:
            positive+=1
            
    print((positive/n))
    print((negative/n))
    print((zero/n))