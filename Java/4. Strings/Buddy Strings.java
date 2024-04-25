/*
Given two strings A and B of lowercase letters, return true if you can swap two letters in A
so the result is equal to B, otherwise, return false.Swapping letters is defined as taking two indices i and j (0-indexed) 
such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
*/


class Solution {
    public boolean buddyStrings(String A, String B) {
        
        for(int i=0;i<A.length()-1;i++){
            for(int j=i+1;j<A.length();j++){
                if(swap(A,i,j).equals(B)){
                    return true;
                }
            }
        }
        
        return false;
    }
    
        String swap(String s,int a,int b){
            char c = s.charAt(a);
            char ch = s.charAt(b);     
            s = s.substring(0,a)+ch+s.substring(a+1);
            s = s.substring(0,b)+c+s.substring(b+1);
            
            return s;
        }
}
