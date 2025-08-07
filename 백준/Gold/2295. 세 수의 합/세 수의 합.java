import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(tokenizer.nextToken());
        Integer[] numbers = new Integer[N];
        Set<Integer> subSet = new HashSet<>();
        Map<Integer, Boolean> isExisted = new HashMap<>();

        for (int i = 0; i < N; i++) {
            tokenizer = new StringTokenizer(br.readLine());
            int number = Integer.parseInt(tokenizer.nextToken());
            numbers[i] = number;
            isExisted.put(number, true);
            for (int j = 0; j <= i; j++) {
                subSet.add(numbers[i] + numbers[j]);
            }
        }

        Arrays.sort(numbers, Comparator.reverseOrder());
        int answer = Arrays.stream(numbers).filter(number -> isMatched(number, subSet, isExisted)).findFirst().get();

        System.out.println(answer);
    }

    private static boolean isMatched(Integer number, Set<Integer> subSet, Map<Integer, Boolean> isExisted) {
        for (int item: subSet) {
            if (!isExisted.containsKey(number - item)) continue;
            return true;
        }

        return false;
    }
}