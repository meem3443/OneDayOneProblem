import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] array = new int[1000];
        int N = sc.nextInt();
        int min=10000;
        int max =0;
        for (int i = 0; i < N; i++) {
            int x = sc.nextInt();
            int dir = sc.nextInt();
            // Please write your code here.
            if(x<min){min=x;}
            if(max<dir){max=dir;}
            while(x<=dir){
                array[x]++;
                x++;
            }
        }
        int result=0;
        //System.out.println(min);
        //System.out.println(max);
        for(int i=min; i<=max ;i++){
            if(array[i]>result){
                result=array[i];
            }
        }
        System.out.print(result);
    }
    
}