/*
A hungry fox, Tim was searching for food and saw a vine of grapes at some distance from him.  Tim was standing at point A when he saw the vine which is at point B. At a time, he can jump a distance of  1m,2m or 5m. 
Help Tim to find out the minimum number of jumps he can have to reach the point.
Input

The first line contains an integer, denoting the number of test cases.

The next lines contain two integers and separated by space.

Output
Print an integer denoting a minimum number of jumps needed.
*/
import java.util.*;
class TestClass {
    public static void main(String args[] ) throws Exception {
        Scanner s = new Scanner(System.in);
        int testcases = s.nextInt();
        while(testcases>0){
            testcases--;
            int a = s.nextInt();
            int b = s.nextInt();
            int difference =  a>b ? (a-b):(b-a);
            int fives = difference/5;
            int two   = (difference%5)/2;
            int ones  = ((difference%5)%2);
            System.out.println(ones+two+fives);
        }

    }
}
