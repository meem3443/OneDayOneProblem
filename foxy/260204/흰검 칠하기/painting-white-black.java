import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int[] W_array = new int[1000000];
        int[] B_array = new int[1000000];
        int[] array =   new int[1000000];
        int point = 500000;
        int min =   500000;
        int max =   500000;

        for (int i = 0; i < N; i++) {
            int x = sc.nextInt();
            char d = sc.next().charAt(0);

            int zero=0;
            while(zero<=x){
                if(zero<x){

                    if(d=='R'){
                        B_array[point]++;
                        array[point]= 1;
                        point++;
                        //System.out.print("B");
                    }
                    else{
                        W_array[point]++;
                        array[point]= -1;
                        point--;
                        //System.out.print("W");
                    }

                    if(max<point){max=point;}
                    if(point<min){min=point;}
                }
                zero++;
            }
            if(d=='R'){point--;}
            else{point++;}
        }

        int result_W=0;
        int result_B=0;
        int result_G=0;

        for(int i=min;i<=max;i++){
            if( 1<W_array[i] && 1<B_array[i]){
                        //array[point]=3;
                        //System.out.print("G");
                        result_G++;
                        continue;
                    }
            if(array[i]==-1){result_W++;}
            if(array[i]== 1){result_B++;}
            //if(array[i]== 3){result_G++;}
        }
        
        System.out.print(result_W+" "+result_B+" "+result_G);
        // Please write your code here.
    }
}