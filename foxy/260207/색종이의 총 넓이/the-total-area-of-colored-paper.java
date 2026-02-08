import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[][] array = new int[1000][1000];
        int point = 500;
        int size =0;

        int[] x = new int[n];
        int[] y = new int[n];
        for (int i = 0; i < n; i++) {
            x[i] = sc.nextInt()+point;
            y[i] = sc.nextInt()+point;
            
            for(int j=x[i]; j<x[i]+8; j++){
                for(int k=y[i]; k<y[i]+8; k++){
                    if( array[j][k]==0 ){
                        size++;
                    }
                    array[j][k]++;
                }
            }
        }
        System.out.print(size);
        // Please write your code here.

        

    }
}