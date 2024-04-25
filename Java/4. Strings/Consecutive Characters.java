/*Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.
Return the power of the string.
Example 1:
Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:
Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
*/
class Solution {
    public int maxPower(String s) {
        int max = 1;
        int temp = 1;
        for(int i=0;i<s.length()-1;i++){
            if(s.charAt(i)==s.charAt(i+1)){
                max++;
                if(max>temp){
                    temp = max;
                }
            }else{
                max = 1;
            }
        }
        return temp;
        
    }
}
