import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        String N = sc.next();
        // Please write your code here.
        int C =0;
        int D =1;

        for(int i= N.length() -1;i>=0;i--){
            int N_num = N.charAt(i) -'0';
            C = C + N_num * D;
            D = D* A;
        }
        //System.out.print(C);

        int B_share =0;
        int B_remian=0;
        String result = "";
        while(C>=1){
            B_remian = C%B;
            C = C/B;
            result = B_remian + result;
        }
        System.out.print(result);

    }
}