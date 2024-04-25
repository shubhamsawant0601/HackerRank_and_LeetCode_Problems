/*You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
*/
class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        
        int planteble = 0;
        
        if(flowerbed.length == 1){
            if(flowerbed[0] == 0)
                planteble++;
        }
        else if(flowerbed.length == 2){
            if(flowerbed[0] == 0 && flowerbed[1]==0) 
                planteble++;
        }
        else if(flowerbed.length == 3){
            if(flowerbed[0]==0 && flowerbed[1]==0 && flowerbed[2]==0)
                planteble = 2;
            else if((flowerbed[0]==0 && flowerbed[1]==0) || (flowerbed[1]==0 && flowerbed[2]==0)) 
                planteble++;    
        }
        else{
            if(flowerbed[0]==0 && flowerbed[1]==0){
               planteble++;
               flowerbed[0] = 1;
            } 
            if(flowerbed[flowerbed.length-1]==0 && flowerbed[flowerbed.length-2]==0){
               planteble++;
               flowerbed[flowerbed.length-1] = 1;
            }
            
            for(int i=1; i<flowerbed.length-1; i++){            
               if(flowerbed[i-1]==0 && flowerbed[i+1]==0 && flowerbed[i]==0){
                    planteble++;
                    flowerbed[i] = 1;
               }
            }
        }
        
        if(planteble >= n){
            return true;
        }
        else{
            return false;
        }
        
    }
}
