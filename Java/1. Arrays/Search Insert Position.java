/*Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1
*/

class Solution {
    public int searchInsert(int[] nums, int target) {
        
        int index = 0;
        int length = nums.length;

        
        for(int i=0;i<length;i++){
          
            if(target <= nums[i]){
                return i;
            }
            else if(target>nums[length-1]){
                return length;
            }
         
        }
        return 0;
    }
}
