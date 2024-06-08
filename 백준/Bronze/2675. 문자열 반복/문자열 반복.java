import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        // 각 테스트 케이스 처리
        for (int t = 0; t < T; t++) {
            // 한 줄을 읽어 공백으로 분리하여 반복 횟수 R과 문자열 S를 구한다
            String[] input = br.readLine().split(" ");
            int R = Integer.parseInt(input[0]);
            String S = input[1];

            // 새 문자열 P를 저장할 StringBuilder
            StringBuilder P = new StringBuilder();

            // 문자열 S의 각 문자를 R번 반복하여 P에 추가
            for (char c : S.toCharArray()) {
                P.append(String.valueOf(c).repeat(R));
            }

            // 결과 출력
            System.out.println(P.toString());
        }
    }
}