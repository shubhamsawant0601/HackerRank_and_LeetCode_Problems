/*Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
*/
class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        int n = word1.length;
        int m = word2.length;
        String s = "";
        String c = "";
        
        for(int i=0;i<n;i++){
            s+=word1[i];
        }
        for(int i=0;i<m;i++){
            c+=word2[i];
        }
        
        if(s.equals(c)){
            return true;
        }else{
            return false;
        }
    }
}
