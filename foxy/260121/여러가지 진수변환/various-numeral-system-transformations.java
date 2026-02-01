import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int b = sc.nextInt();
        // Please write your code here.
        String result = "";
        int remian =0;

        while(n>=1){
            remian = n%b;
            result = ""+ remian +result;
            n = n/b;

        }  
        System.out.print(result);
    }
}