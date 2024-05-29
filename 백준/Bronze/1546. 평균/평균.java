import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // 입력 받기
        int N = scanner.nextInt();
        int[] scores = new int[N];
        
        for (int i = 0; i < N; i++) {
            scores[i] = scanner.nextInt();
        }
        
        // 최댓값 찾기
        int maxScore = 0;
        for (int score : scores) {
            if (score > maxScore) {
                maxScore = score;
            }
        }
        
        // 새로운 점수 계산 및 평균 구하기
        double sum = 0;
        for (int score : scores) {
            double newScore = (double) score / maxScore * 100;
            sum += newScore;
        }
        
        double average = sum / N;
        
        // 결과 출력
        System.out.printf("%.2f", average);
    }
}