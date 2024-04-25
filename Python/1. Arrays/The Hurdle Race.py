"""
Example
height = [1,2,3,3,2]
k = 1

The character can jump 1 unit high initially and must take 3-1=2 doses of potion to be able to jump all of the hurdles.

Sample Input 0

5 4
1 6 3 5 2
Sample Output 0

2
Explanation 0

Dan's character can jump a maximum of k=4 units, but the tallest hurdle has a height of h1=5 :
To be able to jump all the hurdles, Dan must drink 2 doses.

Sample Input 1

5 7
2 5 4 5 2
Sample Output 1

0
Explanation 1

Dan's character can jump a maximum of 7 units, which is enough to cross all the hurdles:

Because he can already jump all the hurdles, Dan needs to drink 0 doses.
"""

def hurdleRace(k, height):
    if max(height)>k:
        return max(height)-k
    else:
        return 0