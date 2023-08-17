import java.util.stream.Collectors;
import java.util.stream.IntStream;

// 1. 10 -> 3진수
// 2. 3진수 뒤집기
// 3. 3진수 -> 10진수
class Solution {
    public String step2(char[] step1){
        return IntStream.range(0, step1.length)
                        .mapToObj(i -> step1[step1.length - 1 - i])
                        .map(Object::toString)
                        .collect(Collectors.joining());
    }
    public int solution(int n) {        
        // 1. 10 -> 3진수
        String step1 = Integer.toString(n, 3);
        
        // 2. 3진수 뒤집기
        String step2 = step2(step1.toCharArray());
        
        return Integer.parseInt(step2, 3);
    }
}