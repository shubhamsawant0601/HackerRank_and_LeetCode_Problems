/*
Armenia and Azerbaijan are in a state of war. Both these countries are separated by a long stretch of mountains of unequal heights. Each country sends its soldiers on the border and these soldiers will have to take position on one of the mountain i.e. 2 mountains will be occupied by two different armies. Uzairovic is a Russian who is acting as a double spy. He asks the Armenians to choose their mountain before the other army chooses theirs but he places two conditions:

1.Armenia will have to march forward and choose a mountain which is largest in height as compared to all the moutains which they have encountered up till now. But in this way, they can choose more than one mountain. So to avoid this, Uzairovic places another condition:

2.Armenia will have to choose the mountain which is the median of all the possible choices from condition 1.

The Armenians are very happy and thank Uzairovic for giving them the advantage of choosing the mountain first. But they don’t know that Uzairovic has planned to plant a bomb in the mountain which will be choosen by Armenia before they arrive there. Help Uzairovic succeed in his mission by giving him the position of the mountain which will decide the fate of the war.

 

Note: Armenia is to the right of mountains below. Positions start from 0, with the mountain closest to Azerbaijan positioned as 0.

Mountains

 

Input:

The first line of input contains an integer n (1<n<1000) – the number of mountains separating the two countries. The next line contains the height of mountains  a[ i ], starting from the mountain closest to Azerbaijan , where 1< a[ i ] < 1000.

Output:

Print an integer that refers to the position of the mountain that will be selected by Armenia. In case of more than one position as your answer, print the one which is closest to Azerbaijan.
*/
import java.util.*;

class TestClass {
    public static void main(String args[] ) throws Exception {
   
     Scanner s = new Scanner(System.in);
     int no    = s.nextInt();
     int arr[] = new int[no];
     int arr2[] = new int[no];
     int index1 = 0, max=0, index2=0;
     
     while(index1 < no){
           arr[index1] = s.nextInt();
           index1++;
        }
  
     for(int i=arr2.length-1;i>=0;i--){
         if(arr[i]>max){
             arr2[index2] = arr[i];
             max = arr[i];
             index2++;
            }
        }
 
     int arr3[] = new int[index2];
     
     for(int i=0;i<arr3.length;i++){
         arr3[i] = arr2[i];
         }

     Arrays.sort(arr3);
     int position = arr3.length/2;
     int mountain = arr3[position]; 

     for(int i=0;i<arr.length;i++){
         if(arr[i]==mountain){
            position = i;
         }
     }
      System.out.println(position);
    }

}    
