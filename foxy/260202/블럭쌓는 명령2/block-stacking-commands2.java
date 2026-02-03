import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int[] array = new int[N];
        for (int i = 0; i < K; i++) {
            int A = sc.nextInt();
            int B = sc.nextInt();

            for(int j=0;j<N;j++){
                if(A<=j && j<=B){
                    array[j-1] = array[j-1] + 1;
                    //System.out.println(array[j]);
                }
            }

        }
        // Please write your code here.
        int result =array[0];

        for (int i = 0; i < N-1 ; i++){
            if(result<array[i+1]){
                result = array[i+1];
            }
        }
        /*
        for (int i = 0; i < N-1 ; i++){
            System.out.println(array[i]);
        }
        */

       System.out.print(result);
    }
}