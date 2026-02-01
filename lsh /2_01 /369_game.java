/*

1. for i가 1부터 N보다 작거나 같을 때까지 1씩 더함
2. if i을 10으로 나머지 연산한 결과가 3, 6, 9 중 하나라면 0 출력
3. else if i을 10으로 나눈 결과를 10으로 나머지 연산한 결과가 3, 6, 9 중 하나라면 0 출력
4. else if i을 3으로 나머지 연산한 결과가 0이라면 0 출력
5. else i 그대로 출력

*/

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for(int i=1; i<=N; i++) {
            if(i%10==3 || i%10==6 || i%10==9) {
                System.out.print("0"+" ");
            } else if((i/10)%10==3 || (i/10)%10==6 || (i/10)%10==9) {
                System.out.print("0"+" ");
            } else if(i%3==0) {
                System.out.print("0"+" ");
            } else {
                System.out.print(i + " ");
            }
            
        }
    }
}
