/*Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.
Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

Example 1:
Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:
Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
*/


class Solution {
    public boolean canThreePartsEqualSum(int[] arr) {
        int sum = 0, count = 0, partSum = 0;
        
        for(int i=0;i<arr.length;i++){
            sum+=arr[i];
        }
        
        if(sum%3==0){
            sum/=3;
        }
        else{
            return false;
        }
        
        for(int i:arr){
            partSum += i;
            if(partSum==sum){
                count++;
                partSum = 0;
            }
        }
        
        return count>=3;
    }
}
