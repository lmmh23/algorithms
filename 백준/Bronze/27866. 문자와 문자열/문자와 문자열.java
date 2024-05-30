import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 스캐너 객체 생성
        Scanner scanner = new Scanner(System.in);
        String x = scanner.nextLine();
        int y = scanner.nextInt();
        
        System.out.print(x.charAt(y - 1));
    }
}