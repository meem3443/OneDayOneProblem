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

        result = result*17;
        //System.out.println(result);


        int[] binary_2 = new int[binary_array.length + 5];
        int share =0;
        int remain =0;
        int index_2=0;

        share = result;
        while(share!=0){
            remain = share%2;
            share = share/2;
            binary_2[index_2++] = remain;
            //System.out.print(index);
        }

        for(int i=index_2 -1; i>=0;i--){
            System.out.print(binary_2[i]);
        }
        if(result==0) System.out.print(result);
        

    }
}