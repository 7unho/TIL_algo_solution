import java.util.*;
import java.util.stream.*;
// 1번 수포자 : 1, 2, 3, 4, 5
// 2번 수포자 - 홀수 : 2
//          - 짝수 : 1, 3, 4, 5
// 3번 수포자 : 3, 3, 1, 1, 2, 2, 4, 4 5

class Solution {
    static int[] count = {0, 0, 0};
    static int[][] patterns = {
        {1, 2, 3, 4, 5},
        {2, 1, 2, 3, 2, 4, 2, 5},
        {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
    };
    public int[] solution(int[] answers) {
        int max = Integer.MIN_VALUE;
        
        for(int i = 0; i < answers.length; i++){
            for(int player = 0; player < 3; player++){
                if(answers[i] == patterns[player][i % (patterns[player].length)] &&
                  ++count[player] > max) max = count[player];
            }
        }
        
        final int MAX = max;
        return IntStream.range(0, 3).filter(i -> count[i] == MAX).map(i -> i + 1).toArray();
    }
}