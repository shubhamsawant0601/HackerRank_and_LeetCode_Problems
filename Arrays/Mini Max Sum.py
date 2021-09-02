"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example arr=[1,3,5,7,9]

min sum = 1+3+5+7
max sum = 3+5+7+9

The minimum sum is  and the maximum sum is . The function prints

16 24
"""

def miniMaxSum(arr):
    print(sum(arr)-max(arr), sum(arr)-min(arr))
