/*
10828(스택)

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

pop
top
push 123
top
pop
top
pop
*/

import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args)throws NumberFormatException, IOException {
		
		// stack 객체 선언
        Stack<Integer> s = new Stack<>();

		//BufferedReader, BufferedWriter 객체 선언
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		// 첫째 줄에 부여하는 명령의 수 n으로 지정
		// scanner 와 다르게 readLine은 String 형태 이므로 형 변환을 해줘야 함
        int x = Integer.parseInt(br.readLine());
		
		// x만큼 반복
        for (int i = 0; i < x; i++) {
			// 명령은 push 123 형태, .split(" ")을 사용 함
			String[] str = br.readLine().split(" ");
			
			// 스위치 문으로 명령마다 행위을 정의해 준다.
            switch (str[0]) {
                case "push":
					
					// 정수 str[1]을 스택에 넣는 연산
                    s.push(Integer.parseInt(str[1]));
                    break;

                case "pop":
				
					// 스택에서 가장 위에 있는 정수를 빼고 그 수를 출력한다.
					// 만약 스택이 비어있을 경우 -1을 출력
                    if (s.empty()) {
					// write함수는 개행문자를 포함하지 안아 줄바꿈을 해주거나 bw.newLine();을 추가해서 줄바꿈 진행 해야한다.
                        bw.write("-1" + "\n");
                    } else {
                        bw.write(s.pop() + "\n");
                    }
                    break;

                case "size":
					
					// 스택에 들어있는 정수 개수 출력
                    bw.write(s.size() + "\n");
                    break;

                case "empty":
				
					// 비어있으면 1출력
                    if (s.empty()) {
                        bw.write("1" + "\n");
                    } else {
                        bw.write("0" + "\n");
                    }
                    break;

                case "top":
				
					// 스택에 가장 위에있는 정수를 출력, 비어있으면 -1 출력
                    if(s.empty()){
                        bw.write("-1"+"\n");
                    } else {
					// 꺼내는게 아닌 출력만 하므로 peek 
                        bw.write(s.peek()+"\n");
                    }
                    break;
            }
        }
        bw.flush();	// 버퍼에 남아 있는 문자열 출력해서 버퍼를 지움
        bw.close(); // 스트림 닫기
    }
}
