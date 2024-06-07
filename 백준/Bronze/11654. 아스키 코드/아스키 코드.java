import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        // 한 글자를 입력받습니다.
        String input = reader.readLine();
        char character = input.charAt(0);
        int asciiValue = (int) character;

        System.out.println(asciiValue);

        reader.close();
    }
}