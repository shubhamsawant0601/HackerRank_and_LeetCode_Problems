/*Given a string s consists of some words separated by spaces, return the length of the last word in the string.
If the last word does not exist, return 0.
A word is a maximal substring consisting of non-space characters only.
Example 1:
Input: s = "Hello World"
Output: 5
Example 2:
Input: s = " "
Output: 0
*/

class Solution {
    public int lengthOfLastWord(String s) {   
        String str[] = s.split(" ");
        int len = str.length;
        
        if(len>1){  
            return str[len-1].length();
        }
        else if(len==1){
            return str[0].length();
        }
        else if(len==0){
            return 0;
        }
        else{
            return 0;
        }
        
    }
}
