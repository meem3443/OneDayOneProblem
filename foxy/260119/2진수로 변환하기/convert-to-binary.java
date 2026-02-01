import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // Please write your code here.

        int[] binary = new int[17];
        int share =0;
        int remain =0;
        int index=0;

        share = n;
        while(share!=0){
            remain = share%2;
            share = share/2;
            binary[index++] = remain;
            //System.out.print(index);
        }
        
        
        for(int i=index -1; i>=0;i--){
            System.out.print(binary[i]);
        }
        if(n==0) System.out.print(n);
    }
}