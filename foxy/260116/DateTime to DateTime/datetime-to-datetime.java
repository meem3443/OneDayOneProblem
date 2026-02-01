import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        // Please write your code here.

        //                                1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
        int[] num_of_days = new int[]{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        
        int d =0;
        int s =0;
        int m =0;
        int result =0;

        if(A<11){
            System.out.print(-1);
        }else if(A<=11 && B<11){
                System.out.print(-1);
            }else if(A<=11 && B<=11 && C<11){
                System.out.print(-1);
            }
            else{
            d = A*24*60;
            s = B*60;
            m = C;
            result = d+s+m;

            result -= (11*24*60) + (11*60) + (11);  

            System.out.print(result);
        }

    }

    }