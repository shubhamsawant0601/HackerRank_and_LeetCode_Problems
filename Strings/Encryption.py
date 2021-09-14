"""
Sample Input 1
feedthedog    

Sample Output 1
fto ehg ee dd

Explanation 1

L=10, sqrt(10)  is between  3 and 4.
Rewritten with  3 rows and 4 columns:

feed
thed
og

Sample Input 2
chillout

Sample Output 2
clu hlt io

Explanation 2

L=8, sqrt(8)  is between 2 and 3.
Rewritten with  3 columns and 3 rows (2*3 < 8 so we have to use 3*3.)

chi
llo
ut
"""


def encryption(s):
    sm=s.replace(" ","")
    st = ""
    r=math.floor(math.sqrt(len(sm)))
    c=math.ceil(math.sqrt(len(sm)))
    for i in range(c):
        st += (sm[i::c]) + " "
        
    return st
                