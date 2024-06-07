import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        // 한 글자를 입력받습니다.
        String input = reader.readLine();
        int N = Integer.parseInt(input);

        int sum = 0;
        input = reader.readLine();
        for (int i = 0; i < N; i++) {
            sum += input.charAt(i) - '0';
        }

        System.out.println(sum);

        reader.close();
    }
}