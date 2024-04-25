/* Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]
*/
class Solution {
    public int[] plusOne(int[] digits) {
        int len = digits.length;
        int temp = 1;

        
        for(int i=len-1;i>=0;i--){
            
            int replaced = (digits[i] + temp)%10;
            
            temp = (temp+digits[i])/10;
            
            digits[i] = replaced;
        }
        
        if(temp>0){
            
            int arr[] = new int[digits.length+1];
            arr[0] = temp;
            for(int i=1; i<len; i++){
                arr[i] = digits[i];
            }
            digits = arr;
        }
        
        return digits;
    }
}
