import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m1 = sc.nextInt();
        int d1 = sc.nextInt();
        int m2 = sc.nextInt();
        int d2 = sc.nextInt();
        // Please write your code here.
        //                                1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
        int[] num_of_days = new int[]{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        
        int result = 0;
        if(m1!=m2){
            result += (num_of_days[m1] -d1);
            for(int i=m1+1; i<m2;i++){
                result += num_of_days[i];
            }
            result += d2;
            result++;
        }else if(m1==m2){
            result = d2-d1;
            result++;
        }
        
        System.out.print(result);
    }
}

