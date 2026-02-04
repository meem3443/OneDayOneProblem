import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int point =500;
        int[] array = new int[1500];
        int min=500;
        int max=500;
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            char y = sc.next().charAt(0);
            int zero=0;
            while(zero<x){
                zero++;
                if(y=='R'){array[point]++; point++;}
                else {array[point-1]++; point--;}

                if(point<min){min=point;}
                if(max<point){max=point;}
            }
        }
        // Please write your code here.

        int result =0;
        //System.out.println(min);
        //System.out.println(max);
        for(int i=min; i<=max;i++){
            if(array[i]>=2){result++;}
            //System.out.println(array[i]);
        }

        System.out.print(result);
    }
}
