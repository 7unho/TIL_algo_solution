import java.util.*;
import java.util.stream.*;
class Solution {
    public int[] solution(int n, long left, long right) {        
        return LongStream.rangeClosed(left, right).mapToInt(item -> (int) Math.max(item/n+1, item%n+1)).toArray();
    }
}