import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m1 = sc.nextInt();
        int d1 = sc.nextInt();
        int m2 = sc.nextInt();
        int d2 = sc.nextInt();
        String A = sc.next();
        // Please write your code here.

        int[] months = new int[]{0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int day=0;

        switch (A) {
        case "Mon": day = 0; break;
        case "Tue": day = 1; break;
        case "Wed": day = 2; break;
        case "Thu": day = 3; break;
        case "Fri": day = 4; break;
        case "Sat": day = 5; break;
        case "Sun": day = 6; break;
    }

        int md1=0;
        int md2=0;

        for(int i=1;i<=12;i++){
            if(i<m1){
                md1 += months[i];
            }
            if(i<m2){
                md2 += months[i];
            }
        }
        md1 += d1;
        md2 += d2;
        
        int sum = md2-md1;
        int result = sum/7;
        //System.out.println(sum);
        //System.out.println(day);
        //System.out.println(sum%7);
        if(sum%7 >= day){result++;}
        
        System.out.print(result);
    
    }
}