import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static int[][] img;
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        img = new int[N][N];

        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            for (int j = 0; j < N; j++) {
                img[i][j] = str.charAt(j) - '0';
            }
        }

        Solution(0, 0, N);
        System.out.println(sb);
    }

    public static void Solution(int x, int y, int size){
        if(isPossible(x, y, size)){
            sb.append(img[x][y]);
            return;
        }

        int newSize = size / 2;

        sb.append('(');

        Solution(x, y, newSize);
        Solution(x, y + newSize, newSize);
        Solution(x + newSize, y, newSize);
        Solution(x + newSize, y + newSize, newSize);

        sb.append(')');
    }

    public static boolean isPossible(int x, int y, int size){
        int value = img[x][y];

        for (int i = x; i < x + size ; i++) {
            for (int j = y; j < y + size; j++) {
                if(value != img[i][j]) return false;
            }
        }
        return true;
    }
}
