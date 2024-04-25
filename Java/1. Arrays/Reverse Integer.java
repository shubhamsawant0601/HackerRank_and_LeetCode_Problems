/*Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:
Input: x = 123
Output: 321
Example 2:
Input: x = -123
Output: -321
*/

class Solution {
    public int reverse(int x) {
        long result = 0;
        long temp   = 0;
        long number = Math.abs(x);
        int sign = (int)(x<0?-1:1);
        while(number>0){
            result = result*10+ number%10;
            number = number/10;     
        }
        if(result>Integer.MAX_VALUE){
            return 0;
        }
        else
        {
            return (int)(result*sign);  
        }      
    }
}
