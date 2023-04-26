import java.io.*;
import java.util.*;

public class Main{

    static HashMap<String, Integer> map;
    public static void main(String[] args)throws NumberFormatException, IOException {

        /*
         *   로마 숫자 => 아라비아 숫자
         *     # 로마 숫자의 각 숫자가 가지는 값을 모두 더한다
         *       다만, IV, IX, XL, XC, CD, CM도 존재
         *
         *       -> 마주치는 로마 숫자의 각 숫자값을 모두 더하 되
         *          이전의 로마숫자값이 작으면 그 이전에 더해진 로마숫자값을 포함하여 그 값을 2번 빼준다
         *          첫 번째 로마 숫자가 두 번째 로마 숫자보다 값이 작다
         *          (이들 외에는 작은 숫자가 큰 숫자 왼쪽 어디에도 나올 수 없다)
         */


        // key, value 값으로 값을 저장
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        map = new HashMap<>(){{
            put("I", 1);
            put("IV", 4);
            put("V", 5);
            put("IX", 9);
            put("X", 10);
            put("XL", 40);
            put("L", 50);
            put("XC", 90);
            put("C", 100);
            put("CD", 400);
            put("D", 500);
            put("CM", 900);
            put("M", 1000);
        }};

        // 저장 된 값을 잘라줌
        String A[] = br.readLine().split("");
        String B[] = br.readLine().split("");

        // 입력된 값 더함
        int sum = getNum(A)+getNum(B);
        String sumRoma = getRoman(sum);
        System.out.println(sum);
        System.out.println(sumRoma);

        br.close();
    }

    // 문자를 하나씩 읽어 가면서 로마 숫자인지 판별 후 res 저장
    static int getNum(String str[]) {
        int res = 0;
        for(int i=0; i<str.length; i++) {

            // 문자열을 아스키로 변환
            char c = str[i].charAt(0);
            if((c=='I'||c=='X'||c=='C'||c=='M')&&i<str.length-1) {
                String tmp = str[i]+str[i+1];

                //key 값에 대한 true false
                if(map.containsKey(tmp)) {
                    res += map.get(tmp);
                    i++;
                    continue;
                }
            }
            res += map.get(str[i]);
        }
        return res;
    }

    static String getRoman(int N) {
        StringBuilder sb = new StringBuilder();
        while(N >= 1000) {
            sb.append("M");
            N -= 1000;
        }
        if(N >= 900) {
            sb.append("CM");
            N -= 900;
        }
        if(N >= 500) {
            sb.append("D");
            N -= 500;
        }
        if(N >= 400) {
            sb.append("CD");
            N -= 400;
        }
        while(N >= 100) {
            sb.append("C");
            N -= 100;
        }
        if(N >= 90) {
            sb.append("XC");
            N -= 90;
        }
        if(N >= 50) {
            sb.append("L");
            N -= 50;
        }
        if(N >= 40) {
            sb.append("XL");
            N -= 40;
        }
        while(N >= 10) {
            sb.append("X");
            N -= 10;
        }
        if(N >= 9) {
            sb.append("IX");
            N -= 9;
        }
        if(N >= 5) {
            sb.append("V");
            N -= 5;
        }
        if(N >= 4) {
            sb.append("IV");
            N -= 4;
        }
        while(N >= 1) {
            sb.append("I");
            N -= 1;
        }
        return sb.toString();
    }
}
