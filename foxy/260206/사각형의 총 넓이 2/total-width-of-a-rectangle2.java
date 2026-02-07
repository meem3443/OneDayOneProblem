import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] array = new int[1000][1000];
        int point =500;
        int size=0;
        
        int[] x1 = new int[n];
        int[] y1 = new int[n];
        int[] x2 = new int[n];
        int[] y2 = new int[n];
        for (int i = 0; i < n; i++) {
            x1[i] = sc.nextInt()+point;
            y1[i] = sc.nextInt()+point;
            x2[i] = sc.nextInt()+point;
            y2[i] = sc.nextInt()+point;

            for(int j=x1[i]; j<x2[i]; j++){
                
                for(int z=y1[i]; z<y2[i]; z++){
                    if( array[j][z] == 0 ){
                        size++;
                    }
                    array[j][z]++;
                    
                }
            }
        }
        System.out.print(size);
        // Please write your code here.
    }
}