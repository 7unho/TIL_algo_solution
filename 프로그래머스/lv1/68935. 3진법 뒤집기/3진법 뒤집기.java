import java.util.stream.Collectors;
import java.util.stream.IntStream;

// 1. 10 -> 3진수
// 2. 3진수 뒤집기
// 3. 3진수 -> 10진수
class Solution {
    public int solution(int n) {
        return Integer.parseInt(new StringBuilder(Integer.toString(n, 3)).reverse().toString(), 3);
    }
}