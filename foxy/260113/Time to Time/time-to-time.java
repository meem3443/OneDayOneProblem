import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
        // Please write your code here.
        
        function(a,b,c,d);



    }

    public static void function(int a,int b,int c,int d){
        int result =0;
        result = (c*60 + d) - (a*60+b); 
        System.out.println(result);
    }
}