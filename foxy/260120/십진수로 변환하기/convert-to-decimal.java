import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String binary = sc.next();
        // Please write your code here.

        char[] binary_array = binary.toCharArray();
        int index = binary_array.length -1;
        int result =0;
        int mul=0;
        int square=1;
        //System.out.println(index);
        for(int i=index;i>=0;i--){
            if(binary_array[i]=='1'){
                result += square*1;
            }
            mul++;
            square = square*2;
            //result += 2*mul * binary_array[i];
        }

        System.out.print(result);

    }
}