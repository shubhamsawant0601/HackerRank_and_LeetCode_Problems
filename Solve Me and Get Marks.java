/* 

INPUT :

The first line has 2 integers N and K  , denoting the number of students in the course  with you and the NoMercy Value chosen by the Proffesor.

The next line contains N integers ,   where ith integer is the marks scored by the ith student in the course. It is guaranteed that all students score non-negative integral marks( highly improbable in Offline semesters ><).

 

OUTPUT :

2 lines should be printed where first and second line should be like

X students need to worry!

Y students should relax!

 
*/
import java.util.*;
class TestClass {
    public static void main(String args[] ) throws Exception {

        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int k = s.nextInt();
        int arr[] = new int[n];
        for(int i=0;i<arr.length;i++){
            arr[i] = s.nextInt();  
        }
        System.out.println(needToWorry(k,arr)+" students need to worry!");
        System.out.println(arr.length-needToWorry(k,arr)+" students should relax!");

    }

    static int needToWorry(int k, int []arr){
        int count=0;
        int arr2 [] = new int[arr.length];
        Arrays.sort(arr);
        for(int i=0;i<arr.length-1;i++){
            if(arr[i+1]-arr[i]<=k){
               arr2[i+1]=1;
               arr2[i] =1;
            }
        }

        for(int i=0;i<arr.length;i++){
            if(arr2[i]==1){
                count++;
            }
        }
        return count;
    }
}
