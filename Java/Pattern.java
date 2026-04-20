import java.util.*;
class Pattern{
    static void patternprint(int r){
        for(int i=0;i<r;i++){
            for(int j=0;j<=i;j++){
                System.out.print("*");
            }
            System.out.println();
        }

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of rows : ");
        int r = sc.nextInt();
        patternprint(r);
    }
}