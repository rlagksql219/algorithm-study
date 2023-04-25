/*
10845(큐)
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front
*/

import java.util.*;
import java.io.*;
public class Main {

    public static void main(String[] args) throws NumberFormatException, IOException {
        //Queue 생성
        Queue<Integer> q = new LinkedList<>();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int x = Integer.parseInt(br.readLine());

        //Queue에서 인덱스 쓸 수 없으므로 마지막 칸에 들어가는 숫자를 last 변수에 넣음
        int last = 0;

        for(int i=0; i<x; i++) {
            String[] str = br.readLine().split(" ");

            switch(str[0]) {
                case ("push") :
                    q.add(Integer.parseInt(str[1]));
                    last = Integer.parseInt(str[1]);
                    break;

                case ("pop") :
                    if(q.isEmpty()) {
                        bw.write("-1" + "\n");
                    } else {
                        bw.write(q.poll() + "\n");
                    }
                    break;

                case ("size") :
                    bw.write(q.size() + "\n");
                    break;

                case ("empty") :
                    if(q.isEmpty()) {
                        bw.write("1" + "\n");
                    } else {
                        bw.write("0" + "\n");
                    }
                    break;

                case ("front") :
                    if(q.isEmpty()) {
                        bw.write("-1" + "\n");
                    } else {
                        bw.write(q.peek() + "\n");
                    }
                    break;

                case ("back") :
                    if(q.isEmpty()) {
                        bw.write("-1" + "\n");
                    } else {
                        bw.write(last + "\n");
                    }
                    break;
            }
        }
        System.out.println(q);
        bw.flush();
        bw.close();
    }
}
