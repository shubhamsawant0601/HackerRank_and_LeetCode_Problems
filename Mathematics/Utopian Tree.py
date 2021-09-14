"""
The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.

A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. How tall will the tree be after n growth cycles?

For example, if the number of growth cycles is n=5, the calculations are as follows:

Sample Input

3
0
1
4
Sample Output

1
2
7
Explanation

There are 3 test cases.

In the first case (n=0), the initial height (H=1) of the tree remains unchanged.

In the second case (n=1), the tree doubles in height and is 2 meters tall after the spring cycle.

In the third case (n=4), the tree doubles its height in spring (n=1,H=2 ), then grows a meter in summer (n=2,H=3), 
then doubles after the next spring (n=3, H=6), and grows another meter after summer (n=4, H=7). Thus, at the end of 4 cycles, its height is 7 meters.
"""
def utopianTree(n):
   
    return ans(n)
    
    
    
def ans(a):
    h = 1
    for i in range(1,a+1):
        if i%2!=0:
            h = h*2
        else:
            h = h+1
        
    return h
