/*Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
*/

class Solution {
    public String longestCommonPrefix(String[] strs) {
        int min = Integer.MAX_VALUE;
        int temp = 0;
        String res = "";
        char ch = 'A' ;
        char ch2 = 'A' ;
        boolean continue1 = false;
        boolean found = true;
        // find shortest String length
        for(int i=0;i<strs.length;i++){
            temp = strs[i].length();
            if(min>temp){
                min = temp;
            }
        }
        // Traverse through Characters of String 
        for(int i=0; i<min;i++){
            // Traverse through Array of String
            for(int j=0;j<strs.length;j++){
                 ch = strs[0].charAt(i);
                ch2 = strs[j].charAt(i);
                
                if(ch2!=ch){
                    continue1 = false;
                    break;
                }
                else
                {
                    continue1 = true;
                }
            }
            // If Character present in all the strings
            
            if(continue1){
                String s = String.valueOf(ch);
                res = res + s;
            }
            else
            {
                break;
            }
        }
        
        return res;
    }
}
