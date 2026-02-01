import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m1 = sc.nextInt();
        int d1 = sc.nextInt();
        int m2 = sc.nextInt();
        int d2 = sc.nextInt();
        // Please write your code here.

        int[] months = new int[]{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int md1 =0;
        int md2 =0;
        int result_num=0;
        
        for(int i=0;i<=12;i++){
            if(i<m1){
                md1 += months[i];
            }
            if(i<m2){
                md2 += months[i];
            }
        }
        md1 += d1;
        md2 += d2;

        if(md1>md2){
             result_num = md1-md2;
             result_num = 7 - (result_num%7);
        }else {
            result_num = md2-md1;
            result_num = result_num%7;
        }
        //System.out.println(md1);
        //System.out.println(md2);
        //System.out.println(result_num);

        switch(result_num ){
        case 0: 
            System.out.print("Mon");
            break;
        case 1: 
            System.out.print("Tue");
            break;
        case 2: 
            System.out.print("Wed");
            break;
        case 3: 
            System.out.print("Thu");
            break;
        case 4: 
            System.out.print("Fri");
            break;
        case 5: 
            System.out.print("Sat");
            break;
        case 6: 
            System.out.print("Sun");
            break;
        }

    }
}