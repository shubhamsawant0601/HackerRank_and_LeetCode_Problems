"""
1528. Shuffle String

Given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
Return the shuffled string.

Example 1:

Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

Example 2:

Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.

Example 3:

Input: s = "aiohn", indices = [3,1,4,2,0]
Output: "nihao"

Example 4:

Input: s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]
Output: "arigatou"

"""




class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # Define string list and dict 
        
        dic = {}
        str_ = []
        
        # Add characters of string as value and indexes as key as keys need to be unique
        
        for i in range(len(indices)):
            dic[indices[i]] = s[i]
            
        # Sort keys of dictionary i.e. indices and append character at that index to str_ list 
        
        for index in  sorted(dic.keys()):
            str_.append(dic[index])
        
        # Return jointed list of str_
        
        return "".join(str_)