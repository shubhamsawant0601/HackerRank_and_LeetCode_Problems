"""
Example. 
s = [a,b,c]
t = [d,e,f]
k = 6

To convert s to t, we first delete all of the characters in 3 moves. Next we add each of the characters of t in order.
 On the 6th move, you will have the matching string. Return Yes.

If there were more moves available, they could have been eliminated by performing multiple deletions on an empty string.
 If there were fewer than 6 moves, we would not have succeeded in creating the new string

Sample Input 0

hackerhappy
hackerrank
9
Sample Output 0

Yes

"""

def appendAndDelete(s, t, k):
    s = [i for i in s]
    t = [i for i in t]
    mini = len(t) if len(s)>len(t) else len(s)
    index = 0
    

    for i in range(mini):
        if s[i]!=t[i]:
            index = i
            break
            
    s1 = s[i:]
    s2 = t[i:]
    
    print(s1, s2)
    
    if (len(s1)+len(s2))<=k  :
        return "Yes"
    else:
        return "No"
        
