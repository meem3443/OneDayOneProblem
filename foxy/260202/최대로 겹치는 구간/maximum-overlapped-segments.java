import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] x1 = new int[n];
        int[] x2 = new int[n];
        for (int i = 0; i < n; i++) {
            x1[i] = sc.nextInt();
            x2[i] = sc.nextInt();
        }
        // Please write your code here.
        int start = 0;
        int end = 0;
        
        for(int i=0;i<n;i++){
            if(start > x1[i]){start= x1[i];}
            if(end < x2[i]){end = x2[i];}
        }

        if(start<0){
            end -= start;
            for (int i = 0; i < n; i++) {
            x1[i] -= start;
            x2[i] -= start;
        }
        }

        int[] result = new int[end+1];

        for(int i=0;i<n;i++){
            for(int j=x1[i];j<x2[i];j++){
                result[j]++;
            }
        }
        int max=0;
        for (int i = 0; i < result.length ; i++) {
            if(result[i]>max){max=result[i];}
        }
        System.out.print(max);
    }
}