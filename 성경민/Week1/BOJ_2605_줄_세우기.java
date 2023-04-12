import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<>();
        int num = sc.nextInt();    
    
        for(int i=0; i<num; i++){
            int num1 = sc.nextInt();
            if(num==0) {
                list.add(i+1);
            }else {
                list.add(list.size()-num1,i+1);
            }
        }
        for(int i : list){
        System.out.print(i+" ");
        }
    }
}
