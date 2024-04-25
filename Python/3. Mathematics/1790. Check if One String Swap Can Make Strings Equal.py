"""
1790. Check if One String Swap Can Make Strings Equal

You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string 
(not necessarily different) and swap the characters at these indices.
Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Answer - 
1. Convert String to list
2. travel through lists and by swapping each character for each position check if strings matches
3. if string matches return true else re-swap to originl position  
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        for i in range(len(s2)):
            for j in range(len(s2)):
                temp = s2[j]
                s2[j] = s2[i]
                s2[i] = temp
                
                if s1 == s2:
                    return True
                    break
                else:
                    temp = s2[j]
                    s2[j] = s2[i]
                    s2[i] = temp
                    
        return False
