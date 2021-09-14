"""
You will be given an array of widths at points along the road (indices), then a list of the indices of entry and exit points. Considering each entry and exit point pair, 
calculate the maximum size vehicle that can travel that segment of the service lane safely.

Example
n = 4
width = [2,3,2,1]
cases = [[1,2],[2,4]]


If the entry index, i=1  and the exit,j=2 , there are two segment widths of 2 and 3 respectively. 
The widest vehicle that can fit through both is 2. If i=2 and j=4, the widths are [3,2,1] which limits vehicle width to 1.

Sample Input

STDIN               Function
-----               --------
8 5                 n = 8, t = 5
2 3 1 2 3 2 3 3     width = [2, 3, 1, 2, 3, 2, 3, 3]
0 3                 cases = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]
4 6
6 7
3 5
0 7
Sample Output

1
2
3
2
1
"""

def serviceLane(n, width, cases):
    li = []
    for c in cases:
        li.append(min(width[ c[0] : c[1]+1 ]))
    
    return li
    