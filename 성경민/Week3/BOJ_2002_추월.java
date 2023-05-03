import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
    /* 처음 등장한다면 hashmap에 차이름과 순서를 넣어준다.
    * 시작 순서는 0번 부터 시작하고 hashmap에 있는 차가 또 나오면 순서를 확인
    * 이후 번호면 cnt를 해줌.
    * inOut 배열에 t/f 표시해준다.
    * 자신이 차례가 맞으면 나오지 않은 순서중 다음 순서로 옮김.
    * */
        BufferedReader //br = new BufferedReader(new InputStreamReader(System.in));
        br = new BufferedReader(new StringReader(src));

        int n = Integer.parseInt(br.readLine());
        HashMap<String, Integer> carList = new HashMap<>();

        for(int i=0;i<n;i++){
            String carName = br.readLine();
            carList.put(carName, i);
        }

        int cnt =0;
        boolean[] inOut = new boolean[n];

        for(int i=0;i<n;i++){
            String carName = br.readLine();
            int num = carList.get(carName);

            for(int j=0;j<num;j++){
                if(!inOut[j]){
                    cnt++;
                    break;
                }
            }
            inOut[num]=true;
        }
        System.out.println(cnt);
        br.close();
    }

    // test data
    static String src = "4\r\n" +
            "ZG431SN\r\n" +
            "ZG5080K\r\n" +
            "ST123D\r\n" +
            "ZG206A\r\n" +
            "ZG206A\r\n" +
            "ZG431SN\r\n" +
            "ZG5080K\r\n" +
            "ST123D";
}
