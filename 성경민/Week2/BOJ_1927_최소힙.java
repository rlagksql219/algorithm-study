/*
1927(최소 힙)
입력에서 0이 주어진 횟수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.

9
0
12345678
1
2
*/
import java.util.*;
import java.io.*;
public class Main {

    public static void main(String[] args) throws NumberFormatException, IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		  int n = Integer.parseInt(br.readLine());
		
		// 우선순위 큐 객체 사용
        PriorityQueue<Integer> q = new PriorityQueue<>();
        for(int i = 0; i < n; i++){
            int num = Integer.parseInt(br.readLine());
            if(num == 0){
                if (q.isEmpty()) {
                    bw.write("0"+"\n");
                } else {
                    bw.write(q.poll() + "\n");
                }
            } else {
                q.add(num);
            }
        }

        bw.flush();
        br.close();
        bw.close();

    }
}
