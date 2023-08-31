import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(int[] numbers) {
        return Arrays.stream(numbers).mapToObj(String::valueOf).sorted((v1, v2) -> {
            int original = Integer.parseInt(v1 + v2);
            int reversed = Integer.parseInt(v2 + v1);
            return reversed - original;
        }).collect(Collectors.joining("")).replaceAll("^0+", "0");
    }
}