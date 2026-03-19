import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        String s = br.readLine();


        LinkedList<Character> l = new LinkedList<>();

        for (char str : s.toCharArray()) {
            l.add(str);
        }


        ListIterator<Character> it = l.listIterator(l.size());

        for (int i = 0; i < m; i++) {
            String command = br.readLine();

            if(command.equals("L")) {
                if(it.hasPrevious()) {
                    it.previous();
                }
            }

            else if(command.equals("R")) {
                if(it.hasNext()){
                    it.next();
                }
            }

            else if(command.equals("D")){
                if(it.hasNext()){
                    it.next();
                    it.remove();
                }
            }
            else if(command.startsWith("P ")){
                char ch = command.charAt(2);
                it.add(ch);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (char ch : l) {
            sb.append(ch);
        }

        System.out.print(sb);
    }
}