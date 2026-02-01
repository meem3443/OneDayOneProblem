import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m1 = sc.nextInt();
        int d1 = sc.nextInt();
        int m2 = sc.nextInt();
        int d2 = sc.nextInt();
        // Please write your code here.

        int months[] = [0,31,28,31,30,31,30,31,31,30,31,30,31];
        int result_num = 0;
        result_num += months[m1]-d1;
        for(int i=m1+1;i<m2;i++){
            result_num+=months[i];
        }
        result_num += d2;

        switch(result_num = result_num%7){
        case 0: break;
        case : break;
        case : break;
        case : break;
        case : break;


        }

    }
}