/*

1. 감기 증상 배열, 체온 배열 만들기
2. 입력값 배열에 저장
3. count 변수 선언
4. 조건에 따라 각 진료소별 count 값 증가
5. countA가 2 이상인 경우 E 추가 출력

*/

import java.util.Scanner;     

public class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        String[] sym = new String[3];
        double[] temp = new double[3];

        for(int i=0; i<temp.length; i++) {
            sym[i] = sc.next();
            temp[i] = sc.nextDouble();
        }

        int countA=0, countB=0, countC=0, countD=0;
        
        for(int i=0; i<temp.length; i++) {

            if(sym[i].equals("Y") && temp[i]>=37) {
                countA++;
            } else if(sym[i].equals("N") && temp[i]>=37) {
                countB++;
            } else if(sym[i].equals("Y") && temp[i]<37) {
                countC++;
            } else {
                countD++;
            }
        }

        System.out.print(countA + " " + countB + " " + countC + " " + countD);
        
        if(countA>=2) {
            System.out.print(" " + 'E');
        }

    }

}
