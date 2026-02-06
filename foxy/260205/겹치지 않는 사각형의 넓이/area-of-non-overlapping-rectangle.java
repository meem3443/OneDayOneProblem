import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int point =1000;
        int ax1 = sc.nextInt()+point;
        int ay1 = sc.nextInt()+point;
        int ax2 = sc.nextInt()+point;
        int ay2 = sc.nextInt()+point;

        int bx1 = sc.nextInt()+point;
        int by1 = sc.nextInt()+point;
        int bx2 = sc.nextInt()+point;
        int by2 = sc.nextInt()+point;

        int mx1 = sc.nextInt()+point;
        int my1 = sc.nextInt()+point;
        int mx2 = sc.nextInt()+point;
        int my2 = sc.nextInt()+point;
        // Please write your code here.
        

        function(ax1,ay1,ax2,ay2,true);
        function(bx1,by1,bx2,by2,true);
        function(mx1,my1,mx2,my2,false);

        System.out.print(size);
    }
    static int size =0;
    static int[][] array = new int[2000][2000];
    static void function(int x1,int y1,int x2,int y2,boolean p){
        for(int i=x1;i<x2;i++){
            for(int j=y1;j<y2;j++){
                if( array[i][j]==0  && p ){ 
                     array[i][j] = 1;
                     //System.out.println("+");
                     size++; 
                }else if( array[i][j]==1 && !p){ 
                    //System.out.println("-");
                    size--;}
            }    
        }
    }


}